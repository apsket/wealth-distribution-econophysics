from __future__ import annotations
import logging
import numpy as np
from typing import Dict, Tuple, Callable, Union
from src.physics import microcanonical_pmf_vectorized, discrete_boltzmann_pmf_infty, discrete_boltzmann_pmf, boltzmann_combinatorial
from src.economy import (
    BaseAgentEconomy,
    Simulator,
    InteractionStrategy
)

logger = logging.getLogger(__name__)


# =====================================================================
#   DYNAMICAL SIMULATION PIPELINE
# =====================================================================

class MarketExperiment:
    """
    A domain-agnostic engine that marries an economy type, a rule-set strategy,
    and an arbitrary suite of analytical models for benchmarking.
    """
    def __init__(
        self,
        economy: BaseAgentEconomy,
        strategy: Union[InteractionStrategy, Callable[[BaseAgentEconomy], bool]],
        num_transactions: int = 2000,
        snapshots: int = 100
    ):
        self.economy = economy
        self.strategy = strategy
        self.snapshots = snapshots
        
        # Calculate timeline bounds directly from the injected economy matrix
        self.num_transactions = num_transactions
        self.simulator = Simulator(system=self.economy, strategy=self.strategy)
        
        # A registry container holding pluggable theoretical math functions
        self._theoretical_models: Dict[str, Callable[[MarketExperiment], np.ndarray]] = {}

    @property
    def wealth_range(self) -> np.ndarray:
        return np.arange(0, self.economy.total_wealth + 1)

    def register_theory(self, label: str, model_func: Callable[[MarketExperiment], np.ndarray]) -> MarketExperiment:
        """Fluent interface to link mathematical models to the validation phase."""
        self._theoretical_models[label] = model_func
        return self

    def execute(self) -> Tuple[np.ndarray, Dict[str, np.ndarray], Dict[str, np.ndarray]]:
        """Runs the concrete simulation setup and evaluates the registered math models."""
        logger.info(f"Launching {self.economy.__class__.__name__}")
        logger.info(f"Processing timeline for {self.num_transactions:,} steps...")
        
        final_wealths, balance_history, history_time = self.simulator.run(steps=self.num_transactions, snapshots=self.snapshots)

        theory_curves = {}    
        for name, math_func in self._theoretical_models.items():
            try:
                theory_curves[name] = math_func(self)
            except Exception as e:
                logger.warning(f"Failed evaluating theoretical model '{name}': {e}", exc_info=True)

        return final_wealths, balance_history, history_time, theory_curves


class EconomyRunner:
    """
    A high-level wrapper to configure, initialize, and execute agent-based 
    wealth distribution experiments with automated theoretical benchmarking.
    """
    def __init__(
        self,
        num_agents: int,
        total_wealth: Union[int, float],
        num_transactions: int,
        economy_cls: type[BaseAgentEconomy],
        strategy: InteractionStrategy,
        snapshots: int = 100
    ):
        self.num_agents = num_agents
        self.total_wealth = total_wealth
        self.num_transactions = num_transactions
        
        # Instantiate the chosen economy model dynamically
        self.economy = economy_cls(
            num_agents=self.num_agents, 
            total_wealth=self.total_wealth
        )
        
        # Bind the strategy and set up the experiment engine
        self.strategy = strategy
        self.experiment = MarketExperiment(
            economy=self.economy, 
            strategy=self.strategy, 
            num_transactions=self.num_transactions,
            snapshots=snapshots
        )
        
        # 3. Automatically register your core theoretical analytical curves
        self._auto_register_theories()

    def _auto_register_theories(self):
        """Registers the standard suite of theoretical PMFs automatically."""
        self.experiment.register_theory(
            "Hybrid Canonical (Infinity)", 
            lambda exp: discrete_boltzmann_pmf_infty(
                m=exp.wealth_range, 
                beta=1.0 / exp.economy.average_wealth
            )
        )
        self.experiment.register_theory(
            "Hybrid Canonical", 
            lambda exp: discrete_boltzmann_pmf(
                m=exp.wealth_range, 
                beta=1.0 / exp.economy.average_wealth, 
                m_total=exp.economy.total_wealth
            )
        )
        self.experiment.register_theory(
            "Canonical Combinatorial", 
            lambda exp: boltzmann_combinatorial(
                m=exp.wealth_range, 
                m_avg=exp.economy.total_wealth / exp.economy.num_agents, 
                m_total=exp.economy.total_wealth
            )
        )
        self.experiment.register_theory(
            "Microcanonical", 
            lambda exp: microcanonical_pmf_vectorized(
                m_array=exp.wealth_range, 
                M=exp.economy.total_wealth, 
                N=exp.economy.num_agents
            )
        )

    def run(self):
        """Executes the simulation pipeline."""
        return self.experiment.execute()

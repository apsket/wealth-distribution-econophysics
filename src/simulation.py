from __future__ import annotations
import logging
import numpy as np
from typing import Dict, Tuple, Callable, Union

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
        self.num_transactions = (self.economy.num_agents * num_transactions) // 2
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
        
        final_wealths, balance_history = self.simulator.run(steps=self.num_transactions, snapshots=self.snapshots)

        theory_curves = {}    
        for name, math_func in self._theoretical_models.items():
            try:
                theory_curves[name] = math_func(self)
            except Exception as e:
                logger.warning(f"Failed evaluating theoretical model '{name}': {e}", exc_info=True)

        return final_wealths, balance_history, theory_curves

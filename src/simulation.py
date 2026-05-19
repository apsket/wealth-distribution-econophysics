from __future__ import annotations
import inspect
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple, List, Callable, Union

# Import your underlying components
from src.economy import (
    BaseAgentEconomy,
    ContinuousStateAgentEconomy,
    DiscreteStateAgentEconomy,
    Simulator,
    InteractionStrategy,
    ContinuousRandomSplit,
    DiscreteRandomSplit
)

# =====================================================================
#   THE PLUGGABLE PIPELINE
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
        self._theoretical_models: Dict[str, Callable[[np.ndarray, float, int], np.ndarray]] = {}

    @property
    def wealth_range(self) -> np.ndarray:
        return np.arange(0, self.economy.total_wealth + 1)

    def register_theory(self, label: str, model_func: Callable[[np.ndarray, float, int], np.ndarray]) -> MarketExperiment:
        """Fluent interface to link mathematical models to the validation phase."""
        self._theoretical_models[label] = model_func
        return self

    def execute(self) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
        """Runs the concrete simulation setup and evaluates the registered math models."""
        print(f"[!] Launching {self.economy.__class__.__name__}")
        print(f"[!] Processing timeline for {self.num_transactions:,} steps...")
        
        final_wealths, balance_history = self.simulator.run(steps=self.num_transactions, snapshots=self.snapshots)

        theory_curves = {}    
        for name, math_func in self._theoretical_models.items():
            try:
                # We pass the entire experiment instance down to the hook
                theory_curves[name] = math_func(self)
            except Exception as e:
                print(f"[Warning] Failed evaluating theoretical model '{name}': {e}")

        return final_wealths, balance_history, theory_curves
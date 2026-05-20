from __future__ import annotations
import numpy as np
import logging
from abc import ABC, abstractmethod
from typing import Callable, Union, Sequence

logger = logging.getLogger("agent_system")


# =====================================================================
#   INTERACTION STRATEGY INTERFACE
# =====================================================================

class InteractionStrategy(ABC):
    """Abstract blueprint for how agents interact and modify system balances."""
    
    @abstractmethod
    def execute_interaction(self, system: BaseAgentEconomy) -> bool:
        """
        Executes a single interaction event between agents.
        Must return True if the system state/balances changed, False otherwise.
        """
        pass


# ----------------------------------------------------------------------------
#   Concrete Strategies
# ----------------------------------------------------------------------------

class ContinuousRandomSplit(InteractionStrategy):
    def execute_interaction(self, system: BaseAgentEconomy) -> bool:
        idx_i, idx_j = system._select_pair()
        total_pot = system.balances[idx_i] + system.balances[idx_j]
        epsilon = np.random.random()
        
        system.balances[idx_i] = np.clip(epsilon * total_pot, 0.0, total_pot)
        system.balances[idx_j] = total_pot - system.balances[idx_i]
        return True


class FixedAmountTransaction(InteractionStrategy):
    def __init__(self, amount: Union[int, float] = 1):
        self.amount = amount

    def execute_interaction(self, system: BaseAgentEconomy) -> bool:
        idx_i, idx_j = system._select_pair()
        if system.balances[idx_i] >= self.amount:
            system.balances[idx_i] -= self.amount
            system.balances[idx_j] += self.amount
            return True
        return False


class DiscreteRandomSplit(InteractionStrategy):
    def execute_interaction(self, system: BaseAgentEconomy) -> bool:
        idx_i, idx_j = system._select_pair()
        w_i = system.balances[idx_i]
        total_pot = w_i + system.balances[idx_j]

        new_i = np.random.randint(0, total_pot + 1)
        if w_i != new_i:
            system.balances[idx_i] = new_i
            system.balances[idx_j] = total_pot - new_i
            return True
        return False
    

class DiscreteTruncatedRandomSplit(InteractionStrategy):
    def execute_interaction(self, system: BaseAgentEconomy) -> bool:
        idx_i, idx_j = system._select_pair()
        w_i = system.balances[idx_i]
        total_pot = w_i + system.balances[idx_j]
        
        new_i = int(np.random.random() * total_pot) # truncated to integer
        if w_i != new_i:
            system.balances[idx_i] = new_i
            system.balances[idx_j] = total_pot - new_i
            return True
        return False


# =====================================================================
#   SYSTEM REPRESENTATION
# =====================================================================

class BaseAgentEconomy(ABC):
    """Abstract base representing a population of agents holding balances."""
    
    def __init__(
        self, 
        num_agents: int = 500, 
        total_wealth: Union[int, float] = 10000, 
        initial_balances: Union[str, Sequence[float], np.ndarray] = "delta"
    ):
        # Validate generic structural inputs (Defensive Gatekeeping)
        if not isinstance(num_agents, int) or num_agents <= 0:
            raise ValueError(f"num_agents must be a positive integer. Got: {num_agents}")
        
        if not isinstance(total_wealth, (int, float)) or total_wealth < 0:
            raise ValueError(f"total_wealth must be a non-negative number. Got: {total_wealth}")
        
        self.num_agents = num_agents
        self.total_wealth = total_wealth
        self.initial_setting = initial_balances

        # 2. Allow subclasses to enforce specific configuration rules (e.g., Integer wealth checks)
        self._validate_subclass_constraints()

        # 3. Build or validate the array and freeze it to self.balances
        self.balances = self._initialize_balances()

    @property
    def average_wealth(self) -> float:
        return self.total_wealth / self.num_agents
    
    def _select_pair(self) -> np.ndarray:
        """Helper method to get indices of two unique agents chosen at random."""
        idx_i, idx_j = np.random.randint(0, self.num_agents, size=2)
        while idx_i == idx_j:
            idx_j = np.random.randint(0, self.num_agents)
        return idx_i, idx_j

    def _initialize_balances(self) -> np.ndarray:
        """Orchestrates generation or explicit validation of initial balances."""
        if self.initial_setting == "delta":
            return self._build_delta_distribution()
        elif self.initial_setting == "uniform":
            return self._build_uniform_distribution()
            
        target_dtype = self._get_native_dtype()
        explicit_array = np.asarray(self.initial_setting, dtype=target_dtype)
        
        # Structural Validation
        if explicit_array.ndim != 1 or len(explicit_array) != self.num_agents:
            raise ValueError(
                f"Injected balances must be a 1D array matching num_agents ({self.num_agents}). "
                f"Got shape {explicit_array.shape}."
            )

        actual_wealth = explicit_array.sum()

        # Micro-Visibility Flag (Triggers on ANY bitwise variance)
        if actual_wealth != self.total_wealth:
            discrepancy = actual_wealth - self.total_wealth
            logger.info(
                f"Initial balance discrepancy detected! "
                f"Configured total_wealth: {self.total_wealth}, "
                f"Actual array sum: {actual_wealth}. "
                f"Absolute drift: {discrepancy:+}"
            )
            
        # Hard Gate Protection (allows for minor floating-point noise)
        if not np.isclose(actual_wealth, self.total_wealth, rtol=1e-7):
            raise ValueError(
                f"Injected balances violate wealth conservation! "
                f"Configured total_wealth is {self.total_wealth}, but array sums to {actual_wealth}."
            )
    
    # --- Abstract Validation and Factory Hooks ---
    @abstractmethod
    def _validate_subclass_constraints(self) -> None:
        """Hook for child classes to validate their specific configuration inputs."""
        pass

    @abstractmethod
    def _get_native_dtype(self) -> type:
        pass

    @abstractmethod
    def _build_delta_distribution(self) -> np.ndarray:
        pass

    @abstractmethod
    def _build_uniform_distribution(self) -> np.ndarray:
        pass


# ----------------------------------------------------------------------------
#   Concrete System States 
# ----------------------------------------------------------------------------

class ContinuousStateAgentEconomy(BaseAgentEconomy):
    """Agents hold continuous, floating-point balances."""

    def _validate_subclass_constraints(self) -> None:
        # Continuous systems natively accept both integer and float wealth amounts
        pass

    def _get_native_dtype(self) -> type:
        return float

    def _build_delta_distribution(self) -> np.ndarray:
        return np.full(self.num_agents, self.total_wealth / self.num_agents, dtype=float)

    def _build_uniform_distribution(self) -> np.ndarray:
        raw_splits = np.random.dirichlet(np.ones(self.num_agents))
        return raw_splits * self.total_wealth


class DiscreteStateAgentEconomy(BaseAgentEconomy):
    """Agents hold discrete, integer balances."""

    def _validate_subclass_constraints(self) -> None:
        # Enforce that total wealth cannot have a fractional decimal component
        if self.total_wealth % 1 != 0:
            raise ValueError(
                f"DiscreteBalanceSystem requires a whole integer total_wealth value. "
                f"Got: {self.total_wealth}"
            )

    def _get_native_dtype(self) -> type:
        return int

    def _build_delta_distribution(self) -> np.ndarray:
        init = np.full(self.num_agents, int(self.total_wealth // self.num_agents), dtype=int)
        init[:int(self.total_wealth % self.num_agents)] += 1
        return init

    def _build_uniform_distribution(self) -> np.ndarray:
        raw_splits = np.random.dirichlet(np.ones(self.num_agents))
        balances = (raw_splits * self.total_wealth).astype(int)
        
        remainder = int(int(self.total_wealth) - balances.sum())
        if remainder > 0:
            indices = np.random.choice(self.num_agents, size=remainder, replace=False)
            balances[indices] += 1
        return balances


# =====================================================================
#   SIMULATION ENGINE
# =====================================================================

class Simulator:
    """Orchestrates the simulation timeline and logs balance history over time."""
    
    def __init__(self, system: BaseAgentEconomy, strategy: Union[InteractionStrategy, Callable[[BaseAgentEconomy], bool]]):
        self.system = system
        self.strategy = strategy
        self.history = []

    def run(self, steps: int = int(1e5), snapshots: int = int(1e2)):
        # Reset system state and clear history
        self.system.balances = self.system._initialize_balances()
        self.history = [self.system.balances.copy()]
        
        # Polymorphically capture whether strategy is a class instance or a raw function
        interaction_runner = (
            self.strategy.execute_interaction 
            if isinstance(self.strategy, InteractionStrategy) 
            else self.strategy
        )

        expected_kind = self.system._get_native_dtype()

        num_events = 0
        while num_events < steps:
            if interaction_runner(self.system):  
                # Type Verification Boundary:
                # np.issubdtype is ideal here because numpy arrays contain types like np.int64 or np.float64, 
                # which are subdtypes of standard Python int and float.
                if not np.issubdtype(self.system.balances.dtype, expected_kind):
                    raise TypeError(
                        f"Interaction strategy mutated system balance array away from its native type! "
                        f"Expected elements of type {expected_kind.__name__}, but array became {self.system.balances.dtype}."
                    )

                num_events += 1
                if num_events % (steps // snapshots) == 0:
                    self.history.append(self.system.balances.copy())
                    
        return self.system.balances, self.history

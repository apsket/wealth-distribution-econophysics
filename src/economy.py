import numpy as np


class ContinuousIdealGasEconomy:
    def __init__(self, num_agents=int(5e2), total_wealth=int(1e4)):
        """
        Models an economy as a gas ensemble.
        """
        self.num_agents = num_agents
        self.total_wealth = total_wealth
        
        # Initialize with perfect equality
        self.accounts = np.full(num_agents, total_wealth / num_agents, dtype=float)

        self.history = [self.accounts.copy()]

    @property
    def average_wealth(self):
        return self.total_wealth / self.num_agents

    def trade(self):
        """Executes a single random trade pair collision."""
        # two unique agents at random
        idx_i, idx_j = np.random.choice(self.num_agents, size=2, replace=False)
        w_i, w_j = self.accounts[idx_i], self.accounts[idx_j]
        
        # calculate total wealth in play for this transaction
        total_pot = w_i + w_j
        
        # random fraction
        epsilon = np.random.random()
        
        # 4. new wealth states
        self.accounts[idx_i] = epsilon * total_pot
        self.accounts[idx_j] = (1 - epsilon) * total_pot

    def simulate(self, steps=int(1e5), snapshots=int(1e2)):
        """Runs the simulation over N trade steps."""
        for s in range(steps):
            self.trade()
            if s % (steps // snapshots) == 0:
                self.history.append(self.accounts.copy())
        return self.accounts


class DiscreteIdealGasEconomy:
    def __init__(self, num_agents=int(5e2), total_wealth=int(1e4)):
        """
        Models an economy as a gas ensemble.
        """
        self.num_agents = num_agents
        self.total_wealth = total_wealth
        
        # Initialize with perfect equality
        self._accounts_init = np.full(num_agents, total_wealth // num_agents, dtype=int)
        self._accounts_init[:total_wealth % num_agents] += 1  # distribute remainder if total_wealth not divisible

        self.accounts = self._accounts_init.copy()
        self.history = [self.accounts.copy()]

    @property
    def average_wealth(self):
        return self.total_wealth / self.num_agents


    def trade(self):
        """Executes a single random trade pair collision."""
        # two unique agents at random
        idx_i, idx_j = np.random.choice(self.num_agents, size=2, replace=False)
        w_i, w_j = self.accounts[idx_i], self.accounts[idx_j]
        
        # calculate total wealth in play for this transaction
        total_pot = w_i + w_j

        # 4. new wealth states
        self.accounts[idx_i] = np.random.randint(0, total_pot + 1)
        self.accounts[idx_j] = total_pot - self.accounts[idx_i]  # ensure total wealth is conserved

        if w_i != self.accounts[idx_i]:  # trade executed if wealth state changes
            return True
        
        return False  # trade not executed due to no change in wealth state


    def simulate(self, steps=int(1e5), snapshots=int(1e2)):
        """Runs the simulation over N trade steps."""

        self.accounts = self._accounts_init.copy()
        self.history = [self._accounts_init.copy()]
    
        num_trades = 0
        while num_trades < steps:
            if self.trade():
                num_trades += 1
                if num_trades % (steps // snapshots) == 0:
                    self.history.append(self.accounts.copy())

        return self.accounts, self.history


    def trade_unitary(self):
        """Executes a single random trade pair collision."""
        # two unique agents at random
        idx_i, idx_j = np.random.choice(self.num_agents, size=2, replace=False)
        w_i = self.accounts[idx_i]

        # 4. new wealth states
        if w_i > 0:
            self.accounts[idx_i] -= 1
            self.accounts[idx_j] += 1

            return True  # trade executed
        
        return False  # trade not executed due to insufficient wealth

    def simulate_unitary_trade(self, steps=int(1e5), snapshots=int(1e2)):
        """Runs the simulation over N trade steps."""

        self.accounts = self._accounts_init.copy()
        self.history = [self._accounts_init.copy()]
        num_trades = 0

        while num_trades < steps:
            if self.trade_unitary():
                num_trades += 1
                if num_trades % (steps // snapshots) == 0:
                    self.history.append(self.accounts.copy())

        return self.accounts, self.history


    def trade_bias_equitable(self):
        """Executes a single random trade pair collision."""
        # two unique agents at random
        idx_i, idx_j = np.random.choice(self.num_agents, size=2, replace=False)
        w_i, w_j = self.accounts[idx_i], self.accounts[idx_j]
        
        # calculate total wealth in play for this transaction
        total_pot = w_i + w_j
        
        # random fraction
        epsilon = np.random.random()

        # 4. new wealth states
        self.accounts[idx_i] = int(epsilon * total_pot)
        self.accounts[idx_j] = total_pot - self.accounts[idx_i]  # ensure total wealth is conserved

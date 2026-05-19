import numpy as np


class BaseGasEconomy:
    def __init__(self, num_agents=int(5e2), total_wealth=int(1e4)):
        self.num_agents = num_agents
        self.total_wealth = total_wealth
        self.accounts = self._initialize_accounts()
        self.history = [self.accounts.copy()]


    @property
    def average_wealth(self):
        return self.total_wealth / self.num_agents


    def _initialize_accounts(self):
        return np.full(self.num_agents, self.total_wealth / self.num_agents, dtype=float)


    def _select_pair(self):
        """Returns indices of two unique agents chosen at random."""
        return np.random.choice(self.num_agents, size=2, replace=False)


    def simulate(self, trade_step_func, steps=int(1e5), snapshots=int(1e2)):
        self.accounts = self._initialize_accounts()
        self.history = [self.accounts.copy()]
        
        num_trades = 0
        while num_trades < steps:
            if trade_step_func():  
                num_trades += 1
                if num_trades % (steps // snapshots) == 0:
                    self.history.append(self.accounts.copy())
                    
        return self.accounts, self.history


class DiscreteEconomy(BaseGasEconomy):
    def _initialize_accounts(self):
        init = np.full(self.num_agents, self.total_wealth // self.num_agents, dtype=int)
        init[:self.total_wealth % self.num_agents] += 1
        return init


    def trade_fixed_amount(self, amount=1):
        idx_i, idx_j = self._select_pair()
        
        if self.accounts[idx_i] >= amount:
            self.accounts[idx_i] -= amount
            self.accounts[idx_j] += amount
            return True
        return False


    def trade_random_split(self):
        idx_i, idx_j = self._select_pair()
        
        w_i = self.accounts[idx_i]
        total_pot = w_i + self.accounts[idx_j]
        new_i = np.random.randint(0, total_pot + 1)
        
        if w_i != new_i:
            self.accounts[idx_i] = new_i
            self.accounts[idx_j] = total_pot - new_i
            return True
        return False
    

    def trade_truncated_random_split(self):
        idx_i, idx_j = self._select_pair()
        
        w_i = self.accounts[idx_i]
        total_pot = w_i + self.accounts[idx_j]
        new_i = int(np.random.random() * total_pot)  # truncated to integer
        
        if w_i != new_i:
            self.accounts[idx_i] = new_i
            self.accounts[idx_j] = total_pot - new_i
            return True
        return False


class ContinuousEconomy(BaseGasEconomy):
    def trade(self):
        idx_i, idx_j = self._select_pair()
        total_pot = self.accounts[idx_i] + self.accounts[idx_j]
        epsilon = np.random.random()
        
        self.accounts[idx_i] = epsilon * total_pot
        self.accounts[idx_j] = (1 - epsilon) * total_pot
        return True     # continuous trades always alter the state

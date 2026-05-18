# Statistical Mechanics of Economic Systems: Predictive Modeling of Wealth Distribution

This project applies the principles of Statistical Physics (specifically the Canonical Ensemble) to model how money moves in a society. By treating agents as "atoms" and money as "energy," we can simulate how microscopic trade rules lead to macroscopic economic patterns—such as the formation of a middle class or the natural emergence of inequality.

We treat the wealth distribution of a society as the most probable configuration of the system.

> The Goal: To demonstrate that wealth distribution is not just a result of social policy, but is driven by principles of entropy and statistical mechanics.


## From Physics to Business
This model translates abstract physical constants into tangible economic indicators.

| Physics Concept |	Economic Equivalent |	Real-World Insight |
| --- | --- | --- |
| Energy (ϵ) | Monetary Unit | Money is conserved in trade, just like energy in a collision. |
| Entropy (S)	| Wealth State Space Volume | A measure of the distinct ways a specific total wealth can be distributed among agents. |
| Beta (β=1/kT)	| Wealth Density | Determines the "Effective Temperature" or purchasing power of a society. |
| Inertia / Mass	| Saving Propensity (λ) | The tendency of agents to hold onto wealth, creating stability. |


## Stages of the Project

### Stage 1: The Zero-Intelligence Economy [Current]

In a "perfect gas" economy where agents trade randomly without saving, wealth naturally follows an Exponential Distribution. This simulation confirms that even in a fair, random system, the most probable wealth state for an individual is zero. Also, inequality is an entropic necessity in a closed system without redistribution

Temperature can be linked to the average wealth.

### Stage 2: The Inertial Economy [Planned]

By introducing a Saving Propensity (λ), we prevent agents from losing everything in a single trade. This transforms the distribution into a Gamma Distribution.

Insight: Saving behavior creates a "hump" in the data, mathematically representing the formation of a middle class.

### Stage 3: The Pareto Tail [Planned]

By varying saving habits across different agents, the model evolves to show a Power Law tail.

Insight: This explains why the "Top 1%" exist in a different statistical class than the rest of the economy.


### Stage 4: The Grand Canonical Economy (Elastic Money Supply) [Planned]

In the current model, the total capital M is strictly conserved, representing a "Gold Standard" or fixed-asset economy. However, modern economies operate with an elastic money supply where credit and central banking allow the total wealth to fluctuate.

In statistical mechanics, this is modeled via the Grand Canonical Ensemble.

#### The Chemical Potential of Money (μ)

Instead of a fixed $M$, we introduce the Chemical Potential, μ. In economics, μ represents the "cost of entry" or the marginal ease of acquiring new money (analogous to interest rates or inflation targets).


## Visualizations
(GIFs here)

Thermalization: Watch how a society starting with 100% equality "melts" into a Boltzmann-Gibbs distribution through random exchange.

The Saving Effect: Watch how the distribution shifts as the saving rate λ is increased from 0 to 0.8.

## Technical Framework
For a deep dive into the mathematical derivations and physics-inspired modeling, please see `docs/`.

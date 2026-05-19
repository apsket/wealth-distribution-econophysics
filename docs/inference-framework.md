# Predictive Modeling & Parametric Inference

This module treats the statistical mechanics simulation as a **synthetic generative engine**. By generating thousands of independent economic histories under varying parameters, we train machine learning models to solve the **Inverse Problem**: inferring microscopic human behavior solely from macroscopic wealth distribution snapshots.

This module treats the statistical mechanics simulation as a synthetic generative engine. By running thousands of forward simulations across a parameter grid, we generate historical macroeconomic snapshots. We then use a multi-tiered architecture—spanning classical information geometry, non-parametric entropic metrics, evolutionary symbolic modeling, and high-capacity machine learning—to solve the Inverse Problem: inferring agent behaviors ($\alpha,\beta$) and economic regimes from macroscopic, noisy wealth distributions.

```math
\mathcal{F}: \{P(m)_{t_0}, P(m)_{t_1}, \dots, P(m)_{t_k}\} \longrightarrow \{\lambda, \mu, \beta\}
```

By balancing classical statistical frameworks with predictive machine learning, we construct an inference pipeline that remains mathematically transparent without sacrificing performance when the system leaves thermodynamic equilibrium.

-------

## Advanced Feature Engineering: Time-Series & Flow Fields

Instead of relying solely on static, isolated snapshots, our framework can extract kinetic signatures by observing how the distribution shifts across a discrete time window $\Delta t$.

### The Microscopic Velocity Field

We map the underlying economic drift by tracking the net flux of agents traversing specific wealth boundaries. For a wealth boundary $m^\*$ the net macro-flux is defined as

$$
\Phi(m^\*) = \sum_{m_i < m^\*} \sum_{m_j \ge m^\*} P(m_i \to m_j) - \sum_{m_i \ge m^\*} \sum_{m_j < m^\*} P(m_i \to m_j)
$$

By tracking this velocity vector, our inference pipeline can differentiate between a Zero-Intelligence Economy and an Inertial Economy ($\lambda \gt 0$), even if their instantaneous macroscopic profiles temporarily mirror one another due to finite-system noise.


## Multi-Tiered Architecture

### Tier 1: Information-Geometric Estimation (Maximum Likelihood GLM)

When the simulation operates close to a known statistical equilibrium, the wealth profile belongs to a strict exponential family.

We use optimization algorithms (such as Nelder-Mead) to maximize the log-likelihood of the empirical wealth vector against the continuous theoretical distribution. The extracted shape parameter ($\alpha$) and scale parameter ($\theta$) map analytically back to the behavioral rules,

$$
\lambda = 1 - \frac{1}{\alpha}, \quad \beta = \frac{1}{\alpha \theta}
$$

Because this tier assumes a perfect parametric family, its prediction error acts as a direct measure of Dynamic Symmetry Breaking: quantifying exactly how much an algorithmic interaction rule deforms the underlying phase space geometry.

### Tier 2: Non-Parametric KNN over Information Manifolds

Standard K-Nearest Neighbors relies on Euclidean distance, which treats histograms as flat, rigid vectors. Because our snapshots are true probability distributions, we implement KNN using an information-theoretic distance metric: Jensen-Shannon (JS) Divergence (the symmetric, numerically stable variant of Kullback-Leibler Divergence).

$$
D_{JS}(P \parallel Q) = \frac{1}{2} D_{KL}\left(P \parallel \frac{P+Q}{2}\right) + \frac{1}{2} D_{KL}\left(Q \parallel \frac{P+Q}{2}\right)
$$

The model queries a historical ledger of simulations run with known ($\lambda,\beta$) pairs. It computes the relative entropy between the unknown society's snapshot and the database entries, averaging the labels of the K closest matches. The advantage of this model is robustness against the small-system fluctuations and finite-size scaling noise found in Phase 3 and Phase 4, without requiring training optimization.


### Tier 3: Interpretative Symbolic Regression

To prevent the pipeline from becoming a black box, we use genetic programming (e.g., via libraries like `gplearn` or `PySR`) to evolve explicit, human-readable algebraic equations.

The evolutionary engine is fed engineered macroscopic statistics (Moments of the distribution: Mean, Variance, Skewness, along with economic indicators like the Gini Coefficient).

The algorithm searches through mathematical operators ($+, −, ×, ÷, \ln{},\exp{}$) to isolate a concise formula mapping macro-indicators back to the hidden micro-rule

$$
\lambda = f(\text{Gini}, \text{Skewness}, \sigma^2)
$$


### Tier 4: Parametric Neural Networks & High-Capacity ML

When heterogeneous saving habits (Stage 3) or elastic credit money supplies (Stage 4) break closed-form analytical assumptions, the system outgrows Tiers 1 and 3. We introduce Neural Networks to learn highly non-linear mappings directly from raw data arrays.

* **1D Convolutional Neural Networks (1D-CNN):** Treats the binned wealth distribution array as a spatial signal. Local convolution filters detect spatial shapes—such as the sharpening of a middle-class "hump" or the elongation of a Pareto tail.

* **Multi-Layer Perceptrons (MLP):** Utilizes fully connected dense layers to map engineered macroscopic feature combinations directly to target parameters.


## Thermodynamic Phase Classification & Non-Ergodic Detection

Alongside parametric regression, the inference engine runs a concurrent classification task to verify structural market integrity. 

* **Objective:** Classify whether an economic system is in a stable state, a transient thermalization phase, or exhibiting dynamic symmetry breaking (e.g., monopolistic collapse or a fractured phase space).

* **Architecture:** Random Forest Classifiers or Support Vector Machines (SVM) trained on engineered macro-features.

* **Target Status Labels:**

    * `Thermalized-Equilibrium`: System perfectly matches maximum entropy expectations.

    * `Metastable-Inertial`: A stable middle class is maintained via saving rules.

    * `Non-Ergodic-Monopoly`: Reversibility is broken; wealth traps have warped the phase space topology.

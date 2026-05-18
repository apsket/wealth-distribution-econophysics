# Micro-Scale Mechanics & The Quantized Limit

## Multi-Scale Convergence and Model Validity Boundaries in an Ideal Gas Economy

This framework establishes the mathematical foundations of a closed economic system using an agent-based statistical mechanics approach. Rather than relying on a single, generalized continuous model, this phase evaluates the system across shifting scales of granularity. By investigating the exact boundary conditions where discrete particle mechanics smooth out into thermodynamic fluid dynamics, we map the structural breakdown and convergence limits of three distinct analytical models.

Assume an economic system of $N$ agents can be modeled as quantized in a fundamental monetary unit $\varepsilon$. The total capital in the society can be described in terms of the total number $M$ of quanta as

```math
E = M\varepsilon
```

## The Hybrid/Naive Canonical Approach (The Continuous Heat-Bath Assumption)

Individual economic actor interact with a massive, continuous system that behaves like an idealized physical heat bath. This enables modeling an agent's wealth distribution through the traditional canonical ensemble.

```math
P(\epsilon) \propto e^{-\epsilon/k T}
```

Because there is only one state per wealth level in this baseline assumption, the density of states is taken as unity throughout.

Defining $\beta = 1/(kT)$ as customary, and under continuity and unbounded assumptions, the thermal energy is found to be

```math
\langle \epsilon \rangle = \int_{0}^{\infty} \epsilon \beta e^{-\beta\epsilon} d\epsilon = \frac{1}{\beta} 
```

Given total wealth is conserved, this implies for the average wealth per capita $\langle \epsilon \rangle = \varepsilon M/N$,

```math
P(\epsilon = m\varepsilon) = \frac{e^{-m\varepsilon/\langle \epsilon \rangle}}{Z} = \frac{\left(e^{-N/M }\right)^{m}}{Z}
```

Where the partition function is captured in discrete space via a geometric progression

```math
Z = \sum_{m=0}^{M} \left(e^{-N/M}\right)^{m} = \frac{1-\left(e^{-N/M}\right)^{M+1}}{1- e^{-N/M}}
```

Here the hybrid/naive approach consists of evaluating the distribution on discrete space while at the same time obtaining a macroscopic variable ($T$) through continuity and unboundedness considerations.

While this continuous "heat-bath" approximation is computationally efficient, it ignores structural boundary restrictions and only partially respects discrete quantization when applied to small or illiquid economic cohorts.

An improvement on small-scale systems can be obtained by a deriving the temperature combinatorially.

## The Canonical Combinatorial Approach (Statistical Temperature)

To account for system boundaries, we can derive a measure of economic temperature directly from its core statistical definition,

```math
\beta = \frac{1}{kT} = \frac{d \ln{\Omega}}{d E} 
```

This requires calculating the exact number of accessible microstates $\Omega$ compatible with a fixed total energy $E$. The problem is equivalent to counting the number of ways to distribute $M$ indistinguishable objects (monetary tokens) into $N$ distinguishable bins (agents). Using Bose-Einstein statistics,

```math
\Omega(M,N) = {{M + N - 1}\choose {M}} = \frac{\left(M + N - 1\right)!}{M!\hspace{0.15cm}\left(N-1\right)!}
```

Applying Stirling's approximation ($\ln{x!}≈x\ln{x}−x$) to scale the natural logarithm of the phase space volume,

$$
\ln{ \Omega(M,N) } = \left(M + N - 1\right) \ln{\left(M + N - 1\right)} - M \ln{M} - \left(N-1\right) \ln{\left(N-1\right)}
$$

Taking the derivative with respect to total energy to isolate the inverse temperature $\beta$,

```math
\frac{d \ln{\Omega}}{dE} = \frac{1}{\varepsilon} \ln{\left(1 + \frac{N-1}{M}\right)}
```

For large populations ($N,M\gg 1$), this expressions simplifies to

```math
\ln{\left(1 + \frac{N-1}{M}\right)} \approx \ln{\left(1 + \frac{N}{M}\right)}
```

The hybrid canonical model can be recovered analytically in the limit where the money supply is significantly larger than the number of agents ($M \gg N$, the high-wealth or fluid limit). Here, the density $N/M \to 0$ allows a first-order Taylor expansion ($\ln{(1+x)} \approx x$),

```math
\beta \approx \frac{1}{\varepsilon} \cdot  \frac{N}{M} = \frac{1}{\langle \epsilon \rangle}
```

For a highly liquid society, the inverse temperature converges precisely to the reciprocal of average wealth.

This sheds light on identifying temperature as average wealth for highly liquid societies. Substituting the discrete combinatorial $\beta$ back into the Boltzmann factor reveals a quantized geometric distribution where $m \in \set{0,1,…,M}$,

```math
P(\epsilon = m\varepsilon) \propto \left( 1 + \frac{N}{M} \right)^{-m}
```

The corresponding partition function evaluates to a truncated discrete geometric series

```math
Z = \sum_{m=0}^{M} \left( \frac{1}{1 + \frac{N}{M}} \right)^{m} = \frac{1 - (1 + N/M)^{-(M+1)}}{1 - (1 + N/M)^{-1}}
```


## The Exact Microcanonical Approach (Finite-System Boundary Mechanics)

For highly quantized, small-scale economic systems where the heat-bath assumption fails entirely, we must abandon canonical approximations. By defining the economy strictly within the microcanonical ensemble, the probability of an agent holding exactly $m$ wealth quanta is calculated purely as the ratio of successful localized microstates to the total phase space volume.

If a single tracking agent isolates a fixed capital of $m$ quanta, the remaining $N-1$ macro-system agents must partition the remaining $M-m$ quanta. The number of degenerate configurations for this isolated sub-system is $\Omega(M-m, N-1)$. 

Thus, the exact, non-approximated microcanonical probability distribution is

```math
P_{\text{micro}}(m) = \frac{\Omega(M-m, N-1)}{\Omega(M,N)} = \frac{\binom{M - m + N - 2}{M - m}}{\binom{M + N - 1}{M}}
```

Expanding the binomial coefficients yields the explicit algebraic formulation,

```math
P_{\text{micro}}(m) = \frac{(M-m+N-2)!}{(M-m)!(N-2)!} \cdot \frac{M!(N-1)!}{(M+N-1)!}
```

Rearranging terms to isolate the product series,

```math
P(m) = (N-1) \frac{M!}{(M-m)!} \frac{(M-m+N-2)!}{(M+N-1)!}
```

By factoring out the structurally independent terms, we can reformulate the microcanonical distribution into an exact product series of conditional probabilities,

```math
P_{\text{micro}}(m) = \frac{N-1}{M+N-1} \prod_{i=1}^{m} \frac{M-i+1}{M+N-1-i}
```

## Multi-Scale Convergence & Thermodynamic Limits

To map the boundary conditions where these three frameworks converge, we evaluate their asymptotic behavior under the traditional thermodynamic limit where the participant population and money supply expand to infinity ($M,N\to \infty$) while maintaining a fixed global wealth density ($\langle\epsilon\rangle/\varepsilon = M/N = c_0$).


### Microcanonical to Combinatorial Canonical Convergence

Evaluating the limit of the exact microcanonical product series,

```math
\begin{gather*}
\lim_{M,N \to \infty} P_{micro} = \left( \frac{N}{M+N} \right) \lim_{M,N \to \infty} \frac{1-(i-1)/M}{1+N/M-(i+1)/M} = \frac{N}{M+N} \left( 1 + \frac{N}{M} \right)^{-m}
\end{gather*}
```

For the canonical combinatorial approach under identical scaling, the partition function simplifies as the truncated boundary term vanishes ($(1+N/M)^{−(M+1)}\to 0$),

$$
\begin{gather*}
\lim_{M,N \to \infty} P_{can-comb} = \left( 1 + \frac{N}{M} \right)^{-m} \lim_{M,N \to \infty} \frac{1 - (1 + N/M)^{-1}}{1 - (1 + N/M)^{-(M+1)}} \\ 
= \left( 1 + \frac{N}{M} \right)^{-m} \lim_{M,N \to \infty} \left( 1 - \left(1 + \frac{N}{M} \right)^{-1} \right) = \left( 1 + \frac{N}{M} \right)^{-m} \frac{N}{M+N}
\end{gather*}
$$

So then

$$
\lim_{M,N \to \infty} P_{micro} \equiv \lim_{M,N \to \infty} P_{can-comb}
$$

This proves that the structural constraints of a closed microcanonical economy smooth out precisely into the combinatorial canonical model when the economic system scales.


### The Hybrid/Naive Canonical Boundary

Now, consider the Hybrid (continuous heat-bath) canonical limit under the same thermodynamic scaling,

$$
\lim_{M,N \to \infty} P_{\text{hybrid}}(m) = \left( e^{-N/M} \right)^m  \lim_{M,N \to \infty} \left[ \frac{1-\left(e^{-N/M}\right)}{1-\left(e^{-N/M}\right)^{M+1}} \right] = \left( e^{-N/M} \right)^m \left( 1 - e^{-N/M} \right)
$$

Without further structural assumptions, the hybrid model remains mathematically distinct from the microcanonical and combinatorial distributions. It only achieves convergence in the highly liquid / high-wealth limit ($M \gg N$), where the wealth density expands toward a continuous fluid. By expanding the exponential terms via first-order Taylor series around zero $e^x \approx 1 + x$,

$$
\lim_{M \gg N} P_{\text{hybrid}}(m) \approx \left( 1 + \frac{N}{M} \right)^{-m} \left( \frac{N}{M+N} \right)
$$

Thus, the hybrid continuous-bath model is an emergent approximation that is valid only when the economy is both thermodynamically large and highly liquid.


### Small-Scale Divergence & Illiquid Structural Breakdown

When simulating micro-scale systems or liquidity-starved token environments where agents and currency units exist in a tight one-to-one parity ($N\approx M$), continuous calculus and heat-bath abstractions break down completely.

To demonstrate this divergence, we isolate the baseline probability of an agent possessing absolutely zero wealth (m=0) in a tight, highly quantized asset ecosystem

| Framework |	Mathematical Form for $P(m=0)$ when $N=M$ |	Asymptotic Value ($M\to\infty$) |
| --- | --- | --- |
| Hybrid Canonical | $\frac{1-e^{-1}}{1- e^{-(M+1)}}$ | $\approx 0.6321$ |
| Canonical Combinatorial	| $\frac{1/2}{1-\left(1/2\right)^{(M+1)}}$ | $\approx 0.5$ |
| Microcanonical | $\frac{M-1}{2M-1}$ | $\approx 0.5$ |

While $P_{can-comb}$ and $P_{micro}$ converge rapidly to 0.5 even for minimal system sizes, the hybrid canonical framework gets trapped at a structurally flawed value of $\approx 0.6321$.

The continuous heat-bath assumption overestimates the probability of complete destitution by over $13\%$. This difference occurs because assuming a continuous, unbounded external reservoir ignores the severe phase space restrictions imposed by actual asset quantization.


## Summary & Literature Context

### The Non-Policy Origin of Inequality

This framework establishes that market inequality is not solely the byproduct of historical, political, or institutional extractions. In a closed, zero-intelligence economy governed by random, conservative trading rules, the system naturally relaxes toward its maximum entropy state: the geometric/exponential distribution. Even when a simulation is initialized with perfect absolute equality ($m=M/N$), the sheer volume of accessible microscopic configurations dictates that the most probable wealth state for an individual agent is always zero. Inequality is an entropic necessity of closed conservation laws.

### Redefining Economic Temperature

Rather than a vague metaphorical descriptor, Economic Temperature (T) is strictly mapped as a function of wealth quantization and density:

$$
\beta = \frac{1}{kT} = \frac{1}{\varepsilon} \ln{\left(1 + \frac{N}{M}\right)}
$$


### Modeling Regimes

* **Illiquid / Quantized Regimes** ($M\approx N$): Temperature is suppressed by structural bounds; discrete combinatorics prevent modeling errors.

* **Fluid / Continuous Regimes*** ($M\gg N$): As liquidity expands, $T\to M/N$. Economic temperature becomes directly synonymous with the per capita average wealth of the population, Dictating the "spread" or volatility of the wealth distribution.


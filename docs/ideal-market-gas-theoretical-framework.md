# Thermal Distribution of Wealth in a Society: "Ideal Gas" (Zero-Intelligence) Economy

Assume an economic system of $N$ agents can be modeled as quantized in fundamental monetary quantity $\varepsilon$. The total capital in the society can be described in terms of the total number $M$ of quanta as

```math
E = M\varepsilon
```

Money plays an analogous role to energy in physical systems under assumptions of conservation.


## Naive Approach

Focusing on an individual agent, its wealth could be approximated by considering its interaction with the economic system as a heat bath. This enables approaching its wealth distrbution through the canonical ensemble. Thus

```math
P(\epsilon) \propto e^{-\epsilon/k T}
```

For its likelihood of having wealth $\epsilon$. Because there is only one state per wealth level, the density of states is unity throughout.

Defining $\beta = 1/(kT)$ as customary, and under continuity and unbounded assumptions, the thermal energy is found to be

```math
\langle \epsilon \rangle = \int_{0}^{\infty} \epsilon \beta e^{-\beta\epsilon} d\epsilon = \frac{1}{\beta} 
```

given total wealth is conserved, this implies $\langle \epsilon \rangle = \varepsilon M/N$

```math
P(\epsilon = m\varepsilon) = \frac{e^{-m\varepsilon/\langle \epsilon \rangle}}{Z} = \frac{\left(e^{-N/M }\right)^{m}}{Z}
```

where the partition function 

```math
Z = \sum_{m=0}^{M} \left(e^{-N/M}\right)^{m} = \frac{1-\left(e^{-N/M}\right)^{M+1}}{1- e^{-N/M}}
```

This will prove a good approximation for the wealth distribution but can be improved by a combinatorial approach to the temperature.

## Combinatorial Approach

To obtain a measure of temperature from its statistical definition
```math
\beta = \frac{1}{kT} = \frac{d \ln{\Omega}}{d E} 
```

The number of microstates $\Omega$ compatible with the macrostate (i.e. in this case, fixed total energy $E$) is required.

The problem is equivalent to counting the number of ways to distribute $n$ indistinguishable objects (i.e. the $M$ monetary exchange units) in $k$ distinguishable groups (i.e. the $N$ agents).

```math
\Omega(M,N) = {{M + N - 1}\choose {M}} = \frac{\left(M + N - 1\right)!}{M!\hspace{0.15cm}\left(N-1\right)!}
```

Taking the natural logarithm and applying Stirling's approximation

```math
\begin{gather*}
\ln{ \Omega(M,N) } = \ln{\left(M + N - 1\right)!} - \ln{M!} - \ln{\left(N-1\right)!} \\
\approx \left(M + N - 1\right) \ln{\left(M + N - 1\right)} - \left(M + N - 1\right) - M \ln{M} + M - \left(N-1\right) \ln{\left(N-1\right)} + \left(N-1\right) \\
= \left(M + N - 1\right) \ln{\left(M + N - 1\right)} - M \ln{M} - \left(N-1\right) \ln{\left(N-1\right)}
\end{gather*}
```

Taking the derivative with respect to the total energy

```math
\begin{gather*}
\frac{d \ln{\Omega}}{dE} = \frac{d \ln{\Omega}}{dM} \cdot \frac{dM}{dE} \\
= \frac{1}{\varepsilon} \left( \ln{\left(M + N - 1\right)} + \left(M + N - 1\right) \frac{1}{M + N - 1} - \ln{M} - M\frac{1}{M} \right) \\
= \frac{1}{\varepsilon} \ln{\left(\frac{M + N - 1}{M}\right)} \\
= \frac{1}{\varepsilon} \ln{\left(1 + \frac{N-1}{M}\right)}
\end{gather*}
```

for large enough $M,N$
```math
\ln{\left(1 + \frac{N-1}{M}\right)} \approx \ln{\left(1 + \frac{N}{M}\right)}
```

where $N/M$ is readily identified as the inverse of average wealth quantum $\langle \epsilon \rangle / \varepsilon$, therefore for the temperature is

```math
\beta = \frac{1}{kT} = \frac{d \ln{\Omega}}{d E} = \frac{1}{\varepsilon} \ln{\left(1 + \frac{N}{M}\right)}
```

The naive approach can be recovered in the limit where the number of units $M$ is much larger than the number of agents $N$ (the "high-wealth" or continuous limit) where $1/\langle \epsilon \rangle \approx 0$, we can use the Taylor expansion $\ln{(1+x)} \approx x$

```math
\beta \approx \frac{1}{\varepsilon} \cdot  \frac{N}{M} = \frac{1}{\langle \epsilon \rangle}
```

For a large, wealthy society, the inverse temperature is exactly the reciprocal of the average wealth.

Using this result into the Boltzmann factor

```math
P(\epsilon) \propto e^{-\epsilon \ln{\left( 1 + N/M \right)} / \varepsilon}
```

Since wealth is quantized in multiples of $\varepsilon$, individual wealth can be expressed as $\epsilon = m\varepsilon$ with $m \in \set{0,1,...,M}$. The most likely distribution of wealth is then given by

```math
P(\epsilon = m\varepsilon) \propto \left( 1 + \frac{N}{M} \right)^{-m}
```

The partition is a truncated geometric series and has a closed analytic form

```math
Z = \sum_{m=0}^{M} \left( \frac{1}{1 + \frac{N}{M}} \right)^{m} = \frac{1 - (1 + N/M)^{-(M+1)}}{1 - (1 + N/M)^{-1}}
```



## Microcanonical Approach


To find the exact probability that an agent has exactly $m$ wealth quanta, we use the ratio of successful microstates to total microstates.

The total accessible microstates $\Omega$ compatible with the macrostate (i.e. in this case, fixed total energy $E$) is required, which we know from the analysis above. If one agent holds exactly $m$ quanta, the remaining $N-1$ agents must share the remaining $M-m$ quanta. 

The number of ways to arrange this remaining sub-system is $\Omega(M-m, N-1)$. Therefore, the exact microcanonical probability distribution for a finite system is:

```math
P(m) = \frac{\Omega(M-m, N-1)}{\Omega(M,N)} = \frac{\binom{M - m + N - 2}{M - m}}{\binom{M + N - 1}{M}}
```

Expanding the binomial coefficients yields the exact, non-approximated analytical solution

```math
P(m) = \frac{(M-m+N-2)!}{(M-m)!(N-2)!} \cdot \frac{M!(N-1)!}{(M+N-1)!}
```

Rearranging terms to isolate the product series

```math
P(m) = (N-1) \frac{M!}{(M-m)!} \frac{(M-m+N-2)!}{(M+N-1)!}
```


## Model Comparissons

The microcanonical probability can be rewritten as a product of $m$ independent and $m$-dependent factors
Rearranging terms to isolate the product series:

```math
P_{micro}(m) = \frac{N-1}{M+N-1} \prod_{i=1}^{m} \frac{M-i+1}{M+N-1-i}
```

In the thermodynamic limit of large society and economy ($M,N \to \infty$) but the average wealth per capita stays the same
```math
\begin{gather*}
\lim_{M,N \to \infty} P_{micro}(m) = \lim_{M,N \to \infty}\frac{N-1}{M+N-1} \prod_{i=1}^{m} \lim_{M,N \to \infty} \frac{M-i+1}{M+N-1-i} = \frac{N}{M+N} \prod_{i=1}^{m} \lim_{M,N \to \infty} \frac{1-i/M+1/M}{1+N/M-1/M-i/M} \\
= \frac{N}{M+N} \prod_{i=1}^{m} \frac{1}{1+N/M} = \frac{N}{M+N} \left( 1 + \frac{N}{M} \right)^{-m}
\end{gather*}
```

While for the canonical combinatorial approach at ($M,N \to \infty$)

```math
\begin{gather*}
\lim_{M,N \to \infty} P_{can-comb} = \left( 1 + \frac{N}{M} \right)^{-m} \lim_{M,N \to \infty} \frac{1 - (1 + N/M)^{-1}}{1 - (1 + N/M)^{-(M+1)}} \\ 
= \left( 1 + \frac{N}{M} \right)^{-m} \left( 1 - \left(1 + \frac{N}{M} \right)^{-1} \right) = \left( 1 + \frac{N}{M} \right)^{-m} \frac{N}{M+N}
\end{gather*}
```

We find the same behavior for the microcanonical and canonical combinatorial distributions in the limit of large systems.

Now for the naive canonical approach in the limit of large systems

```math
\begin{gather*}
\lim_{M,N \to \infty} P_{naive-can} = \lim_{M,N \to \infty} \left(e^{-N/M }\right)^{m} \frac{1-\left(e^{-N/M}\right)}{1-\left(e^{-N/M}\right)^{M+1}} = \left(e^{-N/M }\right)^{m} \left( 1-e^{-N/M} \right)
\end{gather*}
```

The approximations can be carried no further without an average wealth regime. For fixed average wealth per capita, the naive distribution does differ from the canonical combinatorial and microcanonical distributions.

For large $M$ compared to $N$, the Taylor series of the exponential around zero $e^x \approx 1 + x$ shows the naive combinatorial will also converge to the canonical combinatorial thermodynamic limit

```math
\begin{gather*}
\lim_{M,N \to \infty, M \gg N} P_{naive-can} = \lim_{M \gg N} \left(e^{N/M }\right)^{-m} \left( 1-e^{-N/M} \right) = \left(1 + \frac{N}{M} \right)^{-m} \left( 1 - \frac{1}{1+N/M} \right) \\
= \left(1 + \frac{N}{M} \right)^{-m} \left( \frac{N}{M+N} \right)
\end{gather*}
```

So the naive canonical model is equivalent to the other models in the limit of large systems in number of agents and economy and economy significantly larger than the number of agents.

Consider now small systems where $N\approx M$ and the regime of little wealth $m\approx 0$

```math
\begin{gather*}
P_{naive-can}(m=0) = \frac{1-\left(e^{-1}\right)}{1-\left(e^{-1}\right)^{M+1}} = \frac{1-\left(e^{-1}\right)}{1-\left(e^{-1}\right)^{M+1}} \\
P_{can-comb}(m=0) = \frac{1 - (1 + 1)^{-1}}{1 - (1 + 1)^{-(M+1)}} = \frac{1/2}{1+\left(\frac{1}{2}\right)^{(M+1)}} \\
P_{micro}(m=0) = \frac{M-1}{2M-1} \approx \frac{1}{2} - \frac{1}{4(M-1/2)}
\end{gather*}
```

where the Laurent series was used to approximate $P_{micro}(m=0)$. We can readily see that $P_{can-comb}$ and $P_{micro}$ converge quickly to the same value of $1/2$ as $M$ increases, while the naive canonical remains distinct at the small system approximation.


## Summary

### The Spontaneous Emergence of Inequality

In the ideal gas economy if you start a society where every agent has identical wealth (m=M/N), random, conservative trading interactions will inevitably decay into a Gibbs-Boltzmann distribution.

The most probable wealth state for an individual agent is always $m=0$. In a completely un-regulated free market with conservation of currency, exponential inequality is the maximum entropy state.


### The Meaning of Economic "Temperature"

Defining $\beta = \frac{1}{\varepsilon} \ln{\left(1 + \frac{N}{M}\right)}$ reflects average economic wealth as society becomes wealthier $(M\gg N), T \to \frac{M}{N}$. High economic temperature implies a broad, spread-out exponential distribution where high-wealth states are accessible.


### Model Behaviors

The naive canonical, canonical combinatorial and microcanonical approaches converge on the thermodynamic limit of large societies and economies. For small economies, only the canonical combinatorial and microcanonical models agree with each other.


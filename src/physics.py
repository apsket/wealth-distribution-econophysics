import numpy as np
import scipy.special as space


def continuous_boltzmann_pdf(w, beta):
    return beta * np.exp(-beta * w)


def discrete_boltzmann_pmf_infty(m, beta):
    return (1 - np.exp(-beta)) * np.exp(-beta * m)


def discrete_boltzmann_pmf(m, beta, m_max):
    return np.exp(-beta * m) * (1 - np.exp(-beta)) / (1 - np.exp(-beta * (m_max + 1)))


def boltzmann_combinatorial(m, m_avg, m_max):
    geo_ratio = 1 + 1/m_avg
    return (geo_ratio ** (-m)) * (1-geo_ratio**(-1)) / (1 - geo_ratio**(-m_max-1))


def microcanonical_pmf_vectorized(m_array, M, N):
    m_array = np.asarray(m_array)
    valid_mask = (m_array >= 0) & (m_array <= M)
    ln_pmf = np.zeros_like(m_array, dtype=float)
    
    n1 = M - m_array[valid_mask] + N - 2
    k1 = M - m_array[valid_mask]
    ln_num = space.gammaln(n1 + 1) - (space.gammaln(k1 + 1) + space.gammaln(n1 - k1 + 1))
    
    n2 = M + N - 1
    k2 = M
    ln_den = space.gammaln(n2 + 1) - (space.gammaln(k2 + 1) + space.gammaln(n2 - k2 + 1))
    
    ln_pmf[valid_mask] = ln_num - ln_den
    ln_pmf[~valid_mask] = -np.inf
    
    return np.exp(ln_pmf)

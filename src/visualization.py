import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Optional, Tuple


def plot_wealth_distribution(
    final_wealths: np.ndarray,
    theory_dict: Optional[Dict[str, np.ndarray]] = None,
    num_agents: Optional[int] = None,
    transactions: Optional[int] = None,
    plot_title: Optional[str] = 'Thermalization of Wealth',
    figsize: Tuple[float, float] = (7.5, 5.0),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Renders a publication-quality visualization comparing empirical simulation 
    wealth distributions against discrete theoretical markers.
    
    Parameters:
        final_wealths: Array of individual agent wealth states at simulation termination.
        theory_dict: Dictionary mapping model labels to pre-calculated PMF arrays.
                     The array index corresponds to the discrete wealth integer coordinate.
        num_agents: Optional context marker for population size.
        transactions: Optional context marker for step count.
        figsize: Output figure dimensions in inches.
        save_path: If specified, exports the figure directly to disk (e.g., 'figure1.pdf').
    """
    # -------------------------------------------------------------------------
    #   Academic Styling Foundations
    # -------------------------------------------------------------------------
    plt.rcParams.update({
        'font.family': 'serif',
        'text.usetex': False,          
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 9,
        'grid.alpha': 0.20,
        'grid.linestyle': '--'
    })

    fig, ax = plt.subplots(figsize=figsize, dpi=300)
    
    # -------------------------------------------------------------------------
    #   Empirical Histogram Calculation (Unit-Bin Enforcement)
    # -------------------------------------------------------------------------
    min_w = int(np.floor(final_wealths.min()))
    max_w = int(np.ceil(final_wealths.max()))
    
    # Unit bins centered around integer values
    bins = np.arange(min_w, max_w + 2) - 0.5 
    
    # Plot empirical results using a muted, non-distracting background bar profile
    ax.hist(
        final_wealths,
        bins=bins,
        density=True,
        color="#718096",
        alpha=0.20,
        edgecolor="#4A5568",
        linewidth=0.5,
        label="Simulation State (Empirical)"
    )

    # -------------------------------------------------------------------------
    #   Discrete Theoretical Point Overlays
    # -------------------------------------------------------------------------
    if theory_dict:
        # High-contrast, colorblind-friendly academic palette
        colors = ['#E53E3E', '#3182CE', '#DD6B20', '#319795', '#805AD5']
        # Differentiate overlapping theories using diverse geometric markers
        markers = ['o', 's', '^', 'D', 'v']
        
        for i, (label, curve) in enumerate(theory_dict.items()):
            color = colors[i % len(colors)]
            marker = markers[i % len(markers)]
            wealth_coordinates = np.arange(len(curve))
            
            # Scatter explicit points. Modest sizes and edge colors 
            # to keep markers crisp when they overlap on the grid.
            ax.scatter(
                wealth_coordinates, 
                curve, 
                color=color,
                marker=marker,
                s=20,
                zorder=3,
                edgecolor='black',
                linewidths=0.3,
                label=label
            )

    # -------------------------------------------------------------------------
    #   Canvas Polish & Metrology Meta-labels
    # -------------------------------------------------------------------------
    ax.set_xlabel("Agent Wealth ($w$)")
    ax.set_ylabel("Probability $P(w)$")
    ax.set_xlim(left=-0.5, right=max_w + 0.5)
    
    # Main Heading: Set explicitly in bold with a generous pad to clear the subtitle
    ax.set_title(plot_title, weight="bold", pad=24)
    
    # Subtitle: Placed via an absolute coordinate safely nested below the bold title
    if num_agents is not None and transactions is not None:
        subtitle_str = f"$N = {num_agents:,}$ agents  |  $T = {transactions:,}$ interactive events"
        ax.text(
            0.5, 1.02, subtitle_str, 
            transform=ax.transAxes, 
            ha='center', va='bottom', 
            fontsize=9.5, color="#4A5568"
        )

    # Clean border lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(0.8)
    ax.spines['bottom'].set_linewidth(0.8)
    # Inside plot_wealth_distribution
    ax.grid(True, linestyle=':', alpha=0.6, color='#CBD5E1')  # Clean slate grid look
    ax.set_facecolor('#F8FAFC')  # Extremely subtle off-white background block for modern dashboards
    
    # Legend layout
    ax.legend(frameon=True, facecolor="white", edgecolor="none", framealpha=0.8)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
        print(f"[+] Clean graphic successfully archived to: {save_path}")
        
    return fig

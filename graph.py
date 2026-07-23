import numpy as np
import matplotlib.pyplot as plt


def plot_graph(f, a, b):
    """
    Plot the function and shade the integration area.

    Parameters
    ----------
    f : function
        Mathematical function
    a : float
        Lower limit
    b : float
        Upper limit

    Returns
    -------
    matplotlib.figure.Figure
    """

    # Generate x values
    x = np.linspace(a, b, 500)

    # Calculate y values
    y = f(x)

    # Create Figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot Function
    ax.plot(
        x,
        y,
        color="royalblue",
        linewidth=2.5,
        label="f(x)"
    )

    # Shade Integration Area
    ax.fill_between(
        x,
        y,
        0,
        color="skyblue",
        alpha=0.35,
        label="Integration Area"
    )

    # Draw X-axis
    ax.axhline(
        0,
        color="black",
        linewidth=1
    )

    # Draw Y-axis
    ax.axvline(
        0,
        color="black",
        linewidth=1
    )

    # Labels
    ax.set_title(
        "Function Graph",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel(
        "x",
        fontsize=12
    )

    ax.set_ylabel(
        "f(x)",
        fontsize=12
    )

    # Grid
    ax.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    # Legend
    ax.legend()

    # Improve Layout
    plt.tight_layout()

    return fig
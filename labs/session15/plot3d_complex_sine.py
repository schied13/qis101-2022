#!/usr/bin/env python3
# plot3d_complex_sine.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import sys
import os
from IPython.display import Math


def f(x, y):
    # f(z)= abs(ain(z))
    return np.absolute(np.sin(x + y))


def plot(ax):

    # obtaining the real linespace
    x = np.linspace(-2.5, 2.5, 100)
    # obtaining numbers that are of type complex
    y = np.linspace(-1, 1, 100, dtype=complex)
    # assigning j to each complex number
    for idk, val in enumerate(y):
        y[idk] = complex(0, val)

    x, y = np.meshgrid(x, y)

    z = f(x, y)

    #must plot the imaginary part of y in order to be represented on graph
    surf = ax.plot_surface(
        x, np.imag(y), z, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")

    #labeling axes
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(y)")
    ax.set_zlabel("f(z)")

    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()

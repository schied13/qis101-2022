#!/usr/bin/env python3
# plot3d_helix.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):
    theta = np.linspace(0, 20 * np.pi, 2000)  # poloidal angle
    #convert to cartesian coords
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)
    z = theta

    ax.plot(x, y, z)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()

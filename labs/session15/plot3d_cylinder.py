#!/usr/bin/env python3
# plot3d_cylinder.py



import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):

    #toroidal angle
    theta = np.linspace(0, 2 * np.pi, 30) 

    #a cylinder is actually just multiple circles stacked on top of one another therefore we are just adding a z dimension to the equations of a circle
    x = np.sin(theta)
    y = np.cos(theta)
    z = np.outer(np.linspace(0,1,30),np.ones_like(theta))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    
    ax.plot_wireframe(x, y, z)
  


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()

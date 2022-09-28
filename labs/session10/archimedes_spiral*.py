#!/usr/bin/env python3
# archimedes_spiral.py


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import AutoLocator
import os
import sys
import scipy.integrate


def f(x):
    #arc length function that is being integrated
    return np.sqrt(x**2 + 1)

#function that calls scipy to integrate
def arcLength(num):

    result = scipy.integrate.quad(f, 0, num)[0]
    
    return result


def plot(ax):

    theta = np.linspace(0, 8 * np.pi, 1000)
    arc = arcLength(8 * np.pi)
    print(f"Arc length of r = theta :{arc} ")
    #converting r= theta into cartesian coordinates
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)
    ax.plot(x, y, color="red", label=r"$r=\theta$")

    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(AutoLocator())
    ax.grid()
    ax.set_title(r"Archimedes Spiral $r = \theta$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()

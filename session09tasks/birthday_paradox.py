#!/usr/bin/env python3
# birthday_paradox.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from numba import jit
import os
import sys


@jit(nopython=True)
def shared_birthdays(class_size):#function that passes class size through function
    birthdays = np.random.randint(0, 365, class_size)#creates random array of birthdays of size class_size
    #compares each student to each other to see if they share a birthday
    for i in range(birthdays.size - 2):
        for j in range(i + 1, birthdays.size):
            if birthdays[i] == birthdays[j]:
                return True
    return False


@jit(nopython=True)#calculates the probability of shared birthdays in a class 
def calc_probabilities(num_classes, max_class_size):
    prob = np.zeros(max_class_size)
    for class_size in range(max_class_size):
        count = 0
        for _ in range(num_classes):
            if shared_birthdays(class_size):#counts each time we get a shared birthday in a class
                count += 1
        prob[class_size] = count / num_classes# number of times shred birthdays / number of classes 
    return prob


def plot(ax):
    np.random.seed(2021)

    num_classes = 10_000
    max_class_size = 80
    prob = calc_probabilities(num_classes, max_class_size)

    ax.step( # probability is going up use step plot 
        range(max_class_size),
        prob,
        color="black",
        linewidth=3,
        label="Estimated Probability",
    )

    min_class_size = np.where(prob > 0.50)[0][0]#np.where returns back the value of where the conditional is true and the index value(class size in this case)
    p = prob[min_class_size]
    ax.vlines(min_class_size, 0, prob[min_class_size], color="red")

    # See https://en.wikipedia.org/wiki/Birthday_problem
    x = np.linspace(0, 80, 200)
    y = 1 - np.exp(-(x**2) / 730)
    ax.plot(x, y, color="blue", label=r"Approximated: $1-{\rm e}^-\frac{x^2}{365*2}$")

    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1.0)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.grid()
    ax.set_title(f"Birthday Paradox ({num_classes:,} classes)")
    ax.set_xlabel("Class Size")
    ax.set_ylabel("Probability")
    ax.legend()

    ax.annotate(
        f"Min Class Size = {min_class_size}",
        xy=(min_class_size, p),
        xytext=(28, 0.45),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()

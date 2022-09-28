#!/usr/bin/env python3
# bessel_correction.py

import numpy as np
from numpy.random import seed, randint, choice
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from numba import jit
import pickle
import os
import sys

#uses numpy to get population biased variance
@jit(nopython=True)
def get_bsv(arr):
    mean = np.mean(arr)
    bsv = np.sum((arr - mean) ** 2) / len(arr)
    return bsv

#gets the population bsv
@jit(nopython=True)
def get_sample_bsv(population, sample_size):
    num_trials = 20_000
    total_bsv = 0
    for _ in range(num_trials):
        #choice tells you how many items you want from an array of numbers and if you want repeating
        samples = choice(population, sample_size, replace=False)
        total_bsv += get_bsv(samples)
    mean_bsv = total_bsv / num_trials#finds total BSV by dividing each sample bsv by num of trials
    return mean_bsv


def run_trials():
    seed(2021)
    population = randint(0, 1000, 7000)
    pop_var = get_bsv(population)

    max_sample_size = 20

    print(
        f"{'Sample Size':^11}" f"{'Sample Var':^21}" f"{'Pop Var':^18}" f"{'Ratio':^8}"
    )

    results = []
    for sample_size in range(2, max_sample_size + 1):
        sample_bsv = get_sample_bsv(population, sample_size)
        ratio = sample_bsv / pop_var
        results.append((sample_size, sample_bsv, pop_var, ratio))
        print(
            f"{sample_size:^11}" f"{sample_bsv:>16,.4f}" f"{pop_var:>18,.4f}",
            f"{ratio:^15.4f}",
        )
    return results


def plot_ratio(ax, results):
    x = [r[0] for r in results]
    y = [r[3] for r in results]
    ax.plot(x, y, label="BSV/PV")

    x = np.linspace(2, 20, endpoint=True)
    y = (x - 1) / x
    ax.plot(x, y, label=r"$\frac{n-1}{n}$")

    ax.set_title("BSV over PV compared to Hyperbola (n-1) over n")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Biased Sample Var / Population Var")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.legend()


def plot_ubsv(ax, results):
    x = [r[0] for r in results]
    y = [r[2] for r in results]
    ax.plot(x, y, label="Pop Var")

    y = [r[1] for r in results]
    ax.plot(x, y, label="BSV")

    for i, v in enumerate(y):
        y[i] = y[i] * x[i] / (x[i] - 1)
    ax.plot(x, y, label="UBSV")

    ax.set_title("Variance: Population v. Biased Sample v. Unbiased Sample")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Variance")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.legend()


def main():
    #checks for pickle file
    file_name = os.path.dirname(sys.argv[0]) + "/bessel.pickle"
    #if there is no pickle it will create one
    if not os.path.exists(file_name):
        results = run_trials()
        #creates .pickle file
        with open(file_name, "wb") as file_out:
            #stores contents of a list into a file
            pickle.dump(results, file_out, pickle.HIGHEST_PROTOCOL)
        fig = plt.figure(os.path.basename(sys.argv[0]))
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        plot_ratio(ax, results)
        plt.show()
    else:
        with open(file_name, "rb") as file_in:
            results = pickle.load(file_in)

        print(
            f"{'Sample Size':^11}"
            f"{'Sample Var':^21}"
            f"{'Pop Var':^16}"
            f"{'UBSV':^12}"
        )
        for r in results:
            sample_size, sample_bsv, pop_var, _ = r
            ubsv = sample_bsv * sample_size / (sample_size - 1)
            print(
                f"{sample_size:^11}" f"{sample_bsv:>16,.4f}" f"{pop_var:>18,.4f}",
                f"{ubsv:^18,.4f}",
            )

        fig = plt.figure(os.path.basename(sys.argv[0]))
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        plot_ubsv(ax, results)
        plt.show()


if __name__ == "__main__":
    main()

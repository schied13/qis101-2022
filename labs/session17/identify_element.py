#!/usr/bin/env python3
# identify_element.py


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sys
import os


def fit_linear(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    model = LinearRegression().fit(vec_x, vec_y)
    m = model.coef_
    b = model.intercept_
    return m, b


def f(a, b, c, x):
    return a * x**2 + b * x + c


def calc_n(p, t, r):
    return t * ((p) / (r))


def grams_per_mole(m, n):
    return m / n


def plot(ax):
    # Going to need every temperature in kelvin because we are using the
    # ideal gas law to identify the number of moles in the substance
    vec_x = np.array([-50 + 273, 0 + 273, 50 + 273, 100 + 273, 150 + 273])
    vec_y = np.array([11.6, 14.0, 16.2, 19.4, 21.8])

    x = np.linspace(np.min(vec_x), np.max(vec_x), 1000)
    r = 0.0821  # ideal gas constant
    p = 2  # 2.00 atm
    mass = 50  # 50 g of substance

    m, b = fit_linear(vec_x, vec_y)
    ax.plot(x, m * x + b, label="Linear")
    n = calc_n(p, m, r)
    ax.scatter(vec_x, vec_y, color="red")
    gpm = grams_per_mole(mass, n)
    print("Using the slope of the linear regression")
    print("alongside with the Ideal Gas Law")
    print("It can be determined that the gas")
    print(f"Has a molar mass of {float(gpm):.4f} g/mol")
    print("We can then view a periodic table and determine that the gas is Argon")
    print("Argon being the gas that has the molar mass of 39.948 g/mol")
    ax.set_title("Identify Element")
    ax.set_xlabel("Temperature(Kelvin)")
    ax.set_ylabel("Volume(Liters")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()

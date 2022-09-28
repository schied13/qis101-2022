#!/usr/bin/env python3
# lattice_circle.py

import numpy as np
from numba import jit

# See https://en.wikipedia.org/wiki/Gauss_circle_problem


@jit(nopython=True)
def lattice_points(radius):
    num_points = 0#accumulating value set to 0
    radius_squared = radius**2
    for x in range(-radius, radius + 1):# each x value inside the radius
        for y in range(-radius, radius + 1):#each y value inside the radius
            if x**2 + y**2 <= radius_squared:#if the the x and y values squared is less then the radius squared then there is a lattice point inside
                num_points += 1
    return num_points


def main():
    for radius in range(1000, 10001, 1000):#increase radius from 1000 to 10000 in steps of 10000
        act_points = lattice_points(radius)#function to count the number of points
        est_points = int(np.pi * radius**2 + 2 * np.sqrt(2 * np.pi * radius))
        print(
            f"Radius = {radius:>6,}"
            f"  Act Points = {act_points:>12,}"#observed
            f"  Est Points = {est_points:>12,}"#exoected
            f"  % Rel. Err = {(act_points - est_points)/est_points:0.4%}"
        )


if __name__ == "__main__":
    main()

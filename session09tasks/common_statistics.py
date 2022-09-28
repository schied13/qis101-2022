#!/usr/bin/env python3
# common_statistics.py

import numpy as np
import statistics
from collections import Counter


def mean(samples):
    return np.sum(samples) / samples.size


def median(samples):
    #sorts list from small to large
    s = np.sort(samples)
    i = s.size // 2
    #if odd number of elements use the middle element
    if s.size % 2 == 1:
        # Use middle element if length is odd
        m = s[i]
    else:# if even take the average of the two middle elements
        # Use mean of middle two items if length is even
        m = (s[i - 1] + s[i]) / 2
    return m


def mode(samples):
    # Create a dictionary to tally the occurrence of each value
    count = Counter(sorted(samples))#set of key and values where key is the number and the value is how many times it occurs
    # Find the maximum count of all keys (samples)
    max_count = max(count.values())
    # Select the keys which have that max count
    # returns a list of values who have the max_count 
    m = [k for k, v in count.items() if v == max_count]
    return m


def pop_variance(samples):
    m = mean(samples)
    # Numpy n-dimensional arrays are inherently vectorized
    # so element-level arithmetic can be expressed at the array-level
    # without having to loop through each element individually
    v = sum((samples - m) ** 2) / samples.size
    return v


def main():
    np.random.seed(2021)
    samples = np.random.randint(0, 100, 30)
    print(f"Samples      = {samples.tolist()}")    
    print()
    #each compares our way of calculating it and numpy's way of doing it
    print(f"Mean         = {mean(samples):.4f}")
    print(f"Mean         = {np.mean(samples):.4f}")
    print()

    print(f"Median       = {median(samples):.4f}")
    print(f"Median       = {np.median(samples):.4f}")
    print()

    print(f"Mode         = {mode(samples)}")
    print(f"Mode         = {sorted(statistics.multimode(samples))}")
    print()

    v = pop_variance(samples)
    print(f"Pop Variance = {v:.4f}")
    print(f"Pop Variance = {np.var(samples):.4f}")
    print()

    print(f"Pop Std. Dev = {np.sqrt(v):.4f}")
    print(f"Pop Std. Dev = {np.std(samples):.4f}")


if __name__ == "__main__":
    main()

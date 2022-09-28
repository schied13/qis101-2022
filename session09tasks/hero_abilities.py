#!/usr/bin/env python3
# hero_abilities.py

import numpy as np
import random

# To see implementation check calc_stats_1d20
def calc_stats_1d20(num_rolls):
    prng_state = random.getstate()
    mean = 0
    for n in range(0, num_rolls):
        roll = random.randint(3, 18)
        mean += roll
    mean /= num_rolls
    random.setstate(prng_state)
    variance = 0
    for n in range(0, num_rolls):
        roll = random.randint(3, 18)
        variance += pow(roll - mean, 2)
    variance /= num_rolls
    std_dev = np.sqrt(variance)
    return mean, std_dev


def calc_stats_3d6(num_rolls):
    #returns the state of the random number generator
    prng_state = random.getstate()
    mean = 0 #intialize mean to 0 because the value is being collected
    for n in range(0, num_rolls):
        #simulates act of rolling three dice
        roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        mean += roll
    mean /= num_rolls# divides total sum of rolls by num of rolls or calcs mean
    random.setstate(prng_state)# allows random number gen to return the same #'s as before
    variance = 0
    for n in range(0, num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        variance += pow(roll - mean, 2)#calculates the sum portion of the variance
    variance /= num_rolls# calculates variance by / sum and # of rolls
    std_dev = np.sqrt(variance)# stnd dev = (variance)^(1/2)
    return mean, std_dev


def main():
    #random seed
    random.seed(2016)

    #a million rolls
    num_rolls = int(1e6)

    print(f"Rolling abilities for {num_rolls:,} heroes...")

    m1, s1 = calc_stats_1d20(num_rolls)# compacting m1 and s1 into a tuple therefore calc_stats must return a tuple
    m3, s3 = calc_stats_3d6(num_rolls)

    #displays a comparison of mean
    print(f"Mean ability (1d20): {m1:.2f}")
    print(f"Mean ability (3d6):  {m3:.2f}")

    #displays a comparison of std dev
    print(f"Standard Deviation ability (1d20): {s1:.2f}")
    print(f"Standard Deviation ability (3d6) : {s3:.2f}")


if __name__ == "__main__":
    main()

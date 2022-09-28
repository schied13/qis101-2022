#!/usr/bin/env python3
# uniform_variance.py

import random


def run_trial(trial_num):
    trial_lower = random.randint(0, int(1e3))
    trial_upper = 2 * trial_lower + random.randint(0, int(1e3))
    trial_size = random.randint(int(1e6), int(2e6))

    print(f"{trial_num:>10}", end="")
    print(f"{trial_lower:>10,}", end="")
    print(f"{trial_upper:>10,}", end="")
    print(f"{trial_size:>14,}", end="")

    prng_state = random.getstate()
    mean = 0
    for n in range(0, trial_size):
        roll = random.randint(trial_lower, trial_upper)
        mean += roll
    mean /= trial_size

    random.setstate(prng_state)#regenerate random numbers
    variance = 0
    for n in range(0, trial_size):
        roll = random.randint(trial_lower, trial_upper)
        variance += pow(roll - mean, 2)
    variance /= trial_size

    print(f"{mean:>14.3f}", end="")
    print(f"{variance:>14.3f}", end="")

    magic_number = pow(trial_upper - trial_lower, 2) / variance
    print(f"{magic_number:>14.3f}")


def main():
    random.seed(2016)

    print(f"{'Trial #':>10}", end="")
    print(f"{'Lower':>10}", end="")
    print(f"{'Upper':>10}", end="")
    print(f"{'Size':>14}", end="")
    print(f"{'Mean':>14}", end="")
    print(f"{'Variance':>14}", end="")
    print(f"{'Magic':>14}")

    for trial_num in range(1, 16):
        run_trial(trial_num)


if __name__ == "__main__":
    main()

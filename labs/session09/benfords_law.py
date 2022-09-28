#!/usr/bin/env python3
# benfords_law.py
import numpy as np
from numpy.random import seed, randint
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

import os
import sys
import mpmath


def get_first(num):
    count = 0
    k = num 
    while k >0:
        #divides number by 10
        k //=10
        
        #counts number of times divided by 10 to obtain the number of tens places in the number
        count+=1
   
    #formula for first number
    return num/(10**(count-1))


def nums():
    np.random.seed(2016)
    first_nums = np.zeros(10000)
    #through loop 100000 times
    for i in range(0,10000):
        #get random number from 1 to 1e6
        temp = np.random.randint(1,1e6+1)
        #raise that number to the 10th power
        temp = pow(temp,100)
        #at the MSD of that number to the first_nums array
        first_nums[i]= get_first(temp)
        
    return first_nums
        
    

def plot(ax):
    y = nums()
    
    ax.set_title(f"Benford's Law")
    ax.set_xlabel("Number")
    ax.set_ylabel("Count")

    ax.hist(y, bins=8, color="blue",density =True)

    ax.yaxis.set_minor_locator(AutoMinorLocator())

def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()

    




        

if __name__ == "__main__":
    main()

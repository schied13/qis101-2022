#!/usr/bin/env python3
# eulers_constant.py


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import AutoLocator
import os
import sys
import scipy.integrate
import mpmath


mpmath.mp.dps =2000
def f(x):
    # arc length function that is being integrated
    return mpmath.log(mpmath.log(1/x))


# function that calls scipy to integrate
def euler():

    result = -1 * scipy.integrate.quad(f, 0, 1)[0]

    return result



#Calculates the summation as an array
def sums(i):
    sums1 = [0]*50
    for k,val in enumerate(i):

        
        if(k!=0):
            sum = 0
            for s in range(1,k):
                
                sum = sum + 1/s
                
            sums1[k]= sum
            
        else:
            continue
    return sums1

def plot(ax):

    e_constant = euler()
    print(f"Arc length of r = theta :{euler()} ")
    
    #creating equations for gamma plus ln(x)
    x = np.linspace(0,50)
    y = e_constant + np.log(x)

    #creates function of the first 50 harmonic numbers
    x2 = np.linspace(0,50)
    y2 = sums(x2)
   
    ax.plot(x, y, color="blue", label=r"$\gamma + \ln(x)$")
    ax.plot(x2, y2, color="red", label=r"$ \sum^{50}_{x=1} \frac{1}{x}$")
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 5)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(AutoLocator())
    ax.grid()
    ax.set_title(r"Harmonics vs Euler's Constant")
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

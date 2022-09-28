#!/usr/bin/env python3
# maxwell_boltzmann.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import sys



def boltz(a,i):
    #equation for maxwell-botzmann probability density function via https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution
    return np.sqrt(2/np.pi)*(((i**2)*np.exp((-i**2)/(2*(a**2))))/(a**3))

def plot(ax):
    #declares linespace of x being from 0 to 20 with 10000 points
    x= np.linspace(0,20,10000)
    # equation with a = 1
    y = boltz(1,x)
    # equation with a = 2
    y1 = boltz(2,x)
    # equation with a = 5
    y2 = boltz(5,x)
    
    # Plotting the graphs on the main axes
    ax.plot(x,y, color = 'blue')
    ax.plot(x,y1,color = 'red')
    ax.plot(x,y2, color = 'green')
    # Give the graph a title and axis labels
    ax.set_title("$Probability Density Function of the Maxwell-Boltzmann distribution$")  # LaTeX format
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")

    # Center the graph on appropriate range
    ax.set_xlim(0, 20)
    ax.set_ylim(0,.60)
    ax.xaxis.set_major_locator(MultipleLocator(5))

    # Turn on the grid, and add decorations
    ax.grid()
    
   
def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()

    




        

if __name__ == "__main__":
    main()


# Donal Buggy
# program to plot three functions on one graph, calculating f(x)=x, g(x)=x**2, and h(x)=x**3

import matplotlib.pyplot as plt
import numpy as np

# create the numpy array for values 0-4
x = np.arange(0, 5, 1)
print(x)

# define the three functions; each returns the values that will go on the y-axis
def f(x):
    f = x
    return f

def g(x):
    g = x**2
    return g

def h(x):
    h = x**3
    return h

# plot the calculated values, add title, label axes
plt.plot(x, f(x), 'r')
plt.plot(x, g(x), 'y')
plt.plot(x, h(x), 'g')
plt.xlabel("Input values")
plt.ylabel("Output values")
plt.title("Three Functions")

plt.show()

# consulted A Whirlwind Tour of Python, numpy.org (https://numpy.org/devdocs/user/quickstart.html), and scriptverse.academy (https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html) for additional examples of plots
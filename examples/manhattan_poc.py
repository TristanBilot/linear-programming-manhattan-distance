#!/usr/bin/env python3
from manhattan import solve
import matplotlib.pyplot as plt
import numpy as np

r = 5
n = 50
x = np.random.rand(n) * r
y = np.random.rand(n) * r

p = 3
M = [(a, b) for (a, b) in zip(x, y)]

sol = solve(M, p)
solX, solY = np.array(sol).T

plt.xlim(0, r)
plt.ylim(0, r)
plt.scatter(solX, solY, edgecolors='#ee0000', linewidths=5)
plt.scatter(x, y)
plt.show()

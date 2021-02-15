import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from manhattan import solve

r = 10
n = 1000
p = 15
x = np.random.rand(n) * r
y = np.random.rand(n) * r

M = [(a, b) for (a, b) in zip(x, y)]

sol = solve(M, p)
solX, solY = np.array(sol).T

map_img = plt.imread('./content/map.png')
_, ax = plt.subplots(figsize = (8,7))

ax.set_title('Relays ideally placed in Manhattan, {} clients, {} relays.'.format(n, p))
ax.set_xlim(0, r)
ax.set_ylim(0, r)
xs = [x for (x, y) in M]
ys = [y for (x, y) in M]
ax.scatter(xs, ys, zorder=1, alpha= 1, c='b', s=10)
ax.scatter(solX, solY, zorder=2, alpha= 1, color='red', s=70)

ax.imshow(map_img, zorder=0, extent=(0, r, 0, r), aspect='equal')
plt.show()

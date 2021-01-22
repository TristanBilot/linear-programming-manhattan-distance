#!/usr/bin/env python3

from scipy.optimize import linprog

M = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
p = 3

def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)




# obj = [-20, -12, -40, -25]

# lhs_ineq = [[1, 1, 1, 1],  # Manpower
#              [3, 2, 1, 0],  # Material A
#              [0, 1, 2, 3]]  # Material B

# rhs_ineq = [ 50,  # Manpower
#              100,  # Material A
#               90]  # Material B

# opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
#                method="revised simplex")
# print(opt)
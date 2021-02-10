#!/usr/bin/env python3
from scipy.optimize import linprog

# For the moment, solve the optimal point between 
# to other points given the coordinates of those 
# points.
# TODO: use p and M parameters to generate the solution
# based on the user's gieven variables.
def solve():
    C=  [  0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ]
    A=  [
        # dA1
            [ 0, 0, 0, 0, 0, 0, -1, 0, 1, 1, 0, 0 ],
            [ 1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0 ],
            [ -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0 ],
            [ 0, 1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0 ],
            [ 0, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0 ],
        # dA2
            [ 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1],
            [ 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0],
            [ -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0],
            [ 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1],
            [ 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]
        ]
    b=  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    A_eq = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ]
    ]
    b_eq = [ 10, 10, 20, 20 ]
    bounds = [
        (0, None), (0, None), (0, None), (0, None),
        (0, None), (0, None), (0, None), (0, None),
        (0, None), (0, None), (0, None), (0, None)
    ]
    res = linprog(C, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    print(res)

solve()

# soit n le nombre d'acheteurs
# m le nombre de points relais
# c le nombre de contraintes par point acheteur
# vn le nombre de variable associé au nombre d'acheteur (n) = 5
# vm le nombre de variables assoécié au nombre de points relais (m) = 2
# d la dimension des points (x,y) = 2
# A : (n*vn + m*vm, c*(n*vn + m*vm))   : (col, row)
# C : (n*vn + m*vm)
# b : (n*vn + m*vm)
# A_eq : (n*vn + m*vm, n*d)
# b_eq : (n*d)

# 1  var x >= 0;
# 2  var y >= 0;
# 3  var a1 >= 0;
# 4  var b1 >= 0;
# 5  var a2 >= 0;
# 6  var b2 >= 0;
# 7  var d1 >= 0;
# 8  var d2 >= 0;
# 9  var dx1 >= 0;
# 10 var dy1 >= 0;
# 11 var dx2 >= 0;
# 12 var dy2 >= 0;

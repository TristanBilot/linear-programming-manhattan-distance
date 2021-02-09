#!/usr/bin/env python3

from scipy.optimize import linprog

# M = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# p = 3

# def solve(M, p):
#     distances = compute_distances(M)
#     coef = [1, 2]

# def compute_distances(M):
#     n = len(M)
#     distances = []
#     for i in range(n):
#         for j in range(i + 1, n):
#             distances.append(d(M[i], M[j]))
#     return distances

# def d(a, b):
#     x1, y1 = a
#     x2, y2 = b
#     return abs(x1 - x2) + abs(y1 - y2)

# def naive(M):
#     sum = 0
#     n = len(M)
#     for i in range(n):
#         for j in range(n):
#             dist = d(M[i], M[j])
#             if dist > sum:
#                 sum = dist
#     return sum

# print(naive(M))


# pour calculer les contraintes:
#   renseigner dans un dictionnaire les paires (d(a, b), ((xa, ya), (xb, yb)))
#   puis boucler sur le dictionnaire et ajouter aux mêmes indexes les contraintes
#   à l'index i, il faut parcourir le tableau des contraintes sur l'axe des y.



# minimiser dA1 +dA2
# sujetà dA1 ≥ dx,A1 +dy,A1

# dx,A1 ≥ x − a1
# dx,A1 ≥ a1 − x
# dy,A1 ≥ y −b1
# dy,A1 ≥ b1 − y
# dA2 ≥ dx,A2 +dy,A2
# dx,A2 ≥ x − a2
# dx,A2 ≥ a2 − x
# dy,A2 ≥ y −b2subject to c12:    x-a1 <= dx1;
# subject to c13:    a1-x <= dx1;
# subject to c14:    y-b1 <= dy1;
# subject to c15:    b1-y <= dy1;
# dy,A2 ≥ b2 − y


# x − a1 <= d(x,A1)
# x = ? 

# a1 = (3,2)      x(4,3)     -> distance = 1,4
# 4 - 3 = 1 <= 1,4

# minimiser a1 - x + a2 - y + ...

# (a1 - x) + (a2 - y) >= (a1 - x) + (a2 - y)
# (a1 - x) >= x - a1
# (a1 - x) >= a1 - x
# (a2 - y) >= y - b1
# (a2 - y) >= b1 - y







# min(-20x1 - 12x2 - 40x3 -25x4)
# obj = [-20, -12, -40, -25]
# mettre sous forme <=

# lhs_ineq = [[1, 1, 1, 1],  # Manpower
#              [3, 2, 1, 0],  # Material A
#              [0, 1, 2, 3]]  # Material B



# rhs_ineq = [ 50,  # Manpower
#              100,  # Material A
#               90]  # Material B

# opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
#                method="revised simplex")
# print(opt)






# var x >= 0;
# var y >= 0;
# var a1 >= 0;
# var b1 >= 0;
# var a2 >= 0;
# var b2 >= 0;

# minimize z:     a1 - x + b1 - y;

# subject to c11:   a1-x + b1-y >= a1-x + b1-y;
# subject to c12:   a1-x >= x-a1;
# subject to c13:   a1-x >= a1-x;
# subject to c14:   b1-y >= y-b1;
# subject to c15:   b1-y >= b1-y;

# subject to c16:   a1 >= 3;
# subject to c17:   a1 <= 3;
# subject to c18:   b1 <= 5;
# subject to c19:   b1 >= 5;

# subject to c21:   a2-x + b2-y >= a2-x + b2-y;
# subject to c22:   a2-x >= x-a2;
# subject to c23:   a2-x >= a2-x;
# subject to c24:   b2-y >= y-b2;
# subject to c25:   b2-y >= b2-y;

# subject to c26:   a2 >= 6;
# subject to c27:   a2 <= 6;
# subject to c28:   b2 <= 10;
# subject to c29:   b2 >= 10;

# end;

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

res = linprog(C, A_ub=A, b_ub=b, bounds=
    [
        (0, None), (0, None), (0, None), (0, None),
        (0, None), (0, None), (0, None), (0, None),
        (0, None), (0, None), (0, None), (0, None)
    ])
print(res)

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


# minimize z:        d1 + d2 + d3;

# # dA1
# subject to c11:    dx1 + dy1 <= d1;
# subject to c12:    x-a1 <= dx1;
# subject to c13:    a1-x <= dx1;
# subject to c14:    y-b1 <= dy1;
# subject to c15:    b1-y <= dy1;

# subject to c61:    -(dx1 + dy1) <= d1;
# subject to c62:    -(x-a1) <= dx1;
# subject to c63:    -(a1-x) <= dx1;
# subject to c64:    -(y-b1) <= dy1;
# subject to c65:    -(b1-y) <= dy1;

# [0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, 0]
# [-1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0]
# [1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0]
# [0, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0]
# [0, 1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0]



# # dA2
# subject to c21:    dx2 + dy2 <= d2;
# subject to c22:    x-a2 <= dx2;
# subject to c23:    a2-x <= dx2;
# subject to c24:    y-b2 <= dy2;
# subject to c25:    b2-y <= dy2;



# subject to c71:    -(dx2 + dy2) <= d2;
# subject to c72:    -(x-a2) <= dx2;
# subject to c73:    -(a2-x) <= dx2;
# subject to c74:    -(y-b2) <= dy2;
# subject to c75:    -(b2-y) <= dy2;


# [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 1]
# [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0]
# [1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0]
# [0, -1, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0]
# [0, 1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0]

# subject to c106:   a1 >= 6;
# subject to c107:   a1 <= 6;
# subject to c108:   b1 <= 10;
# subject to c109:   b1 >= 10;

# subject to c96:   a2 >= 12;
# subject to c97:   a2 <= 12;
# subject to c98:   b2 <= 20;
# subject to c99:   b2 >= 20;


# end;
#!/usr/bin/env python3

from scipy.optimize import linprog

M = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
p = 3

def solve(M, p):
    distances = compute_distances(M)
    coef = [1, 2]

def compute_distances(M):
    n = len(M)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            distances.append(d(M[i], M[j]))
    return distances

def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

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
# dy,A2 ≥ y −b2
# dy,A2 ≥ b2 − y


x − a1 <= d(x,A1)
x = ? 

a1 = (3,2)      x(4,3)     -> distance = 1,4
4 - 3 = 1 <= 1,4

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



var x >= 0;
var y >= 0;
var a1 >= 0;
var b1 >= 0;
var a2 >= 0;
var b2 >= 0;
var a3 >= 0;
var b3 >= 0;
var d1 >= 0;
var d2 >= 0;
var d3 >= 0;
var dx1 >= 0;
var dy1 >= 0;
var dx2 >= 0;
var dy2 >= 0;
var dx3 >= 0;
var dy3 >= 0;

minimize z:     d1 + d2 + d3; #(a1 - x + b1 - y) + (a2 - x + b2 - y);

# dA1
subject to c11:   d1 >= dx1 + dy1; # a1-x + b1-y >= x-a1 + y-b1;
subject to c12:   dx1 >= x-a1; # x-a1
subject to c13:   dx1 >= a1-x;
subject to c14:   dy1 >= y-b1; #b1-y
subject to c15:   dy1 >= b1-y;

subject to c61:   d1 >= -(dx1 + dy1);
subject to c62:   dx1 >= -(x-a1);
subject to c63:   dx1 >= -(a1-x);
subject to c64:   dy1 >= -(y-b1);
subject to c65:   dy1 >= -(b1-y);

# dA2
subject to c21:   d2 >= dx2 + dy2; # a2-x + b2-y
subject to c22:   dx2 >= x-a2;
subject to c23:   dx2 >= a2-x;
subject to c24:   dy2 >= y-b2;
subject to c25:   dy2 >= b2-y;

subject to c71:   d2 >= -(dx2 + dy2);
subject to c72:   dx2 >= -(x-a2);
subject to c73:   dx2 >= -(a2-x);
subject to c74:   dy2 >= -(y-b2);
subject to c75:   dy2 >= -(b2-y);

# dA3
subject to c111:   d3 >= dx3 + dy3; # a3-x + b3-y
subject to c112:   dx3 >= x-a3;
subject to c113:   dx3 >= a3-x;
subject to c114:   dy3 >= y-b3;
subject to c115:   dy3 >= b3-y;

subject to c131:   d3 >= -(dx3 + dy3);
subject to c132:   dx3 >= -(x-a3);
subject to c133:   dx3 >= -(a3-x);
subject to c134:   dy3 >= -(y-b3);
subject to c135:   dy3 >= -(b3-y);


subject to c106:   a1 >= 6;
subject to c107:   a1 <= 6;
subject to c108:   b1 <= 10;
subject to c109:   b1 >= 10;

subject to c96:   a2 >= 12;
subject to c97:   a2 <= 12;
subject to c98:   b2 <= 20;
subject to c99:   b2 >= 20;

subject to c140:   a3 >= 28;
subject to c141:   a3 <= 28;
subject to c142:   b3 <= 43;
subject to c143:   b3 >= 43;


# end;
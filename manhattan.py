#!/usr/bin/env python3
from typing import List, Tuple
from scipy.optimize import linprog

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

def format_equation(M: List[Tuple[float, float]], p: int) -> List[float]:
    """
    Returns the equation C to minimize, built from the list of clients and
    the number of stations to consider.
    """
    C = [0 for _ in range(2*p + 2*len(M) + len(M)*p + 2*len(M))]
    start = 2*p + 2*len(M)
    end = start + len(M)*p
    for i in range(start, end):
        C[i] = 1
    return C
    

# subject to c11:    dx1 + dy1 <= d1;
# subject to c12:    x-a1 <= dx1;
# subject to c13:    a1-x <= dx1;
# subject to c14:    y-b1 <= dy1;
# subject to c15:    b1-y <= dy1;
def format_left_in(M: List[Tuple[float, float]], p: int) -> List[float]:
    """
    Returns the lhs of the inequation matrix, considering also the rhs variables
    for simplicity purpose.
    """
    A = [[0 for i in range(len(M)*(4+p)+p*2)] for _ in range(len(M)*5*p)]
    x = 0
    y = 1
    d = p*2 + len(M)*2
    a = p*2
    b = p*2 + 1
    dx = p*2+ len(M)*(2+p)
    dy = p*2+ len(M)*3 + 1
    it = 0
    for i in range(0, len(M)*p):
        # constraint 1
        A[it][dx] = 1
        A[it][dy] = 1
        A[it][d] = -1
        # constraint 2
        A[it+1][x] = 1
        A[it+1][a] = -1
        A[it+1][dx] = -1
        # constraint 3
        A[it+2][x] = -1
        A[it+2][a] = 1
        A[it+2][dx] = -1
        # constraint 4
        A[it+3][y] = 1
        A[it+3][b] = -1
        A[it+3][dy] = -1
        # constraint 5
        A[it+4][y] = -1
        A[it+4][b] = 1
        A[it+4][dy] = -1
        #update indexes
        # consider the next (xi,yi) when the last element is reached
        if i % len(M) == len(M)-1:
            x += 2
            y += 2
            d = p*2 + len(M)*2
            a = p*2
            b = p*2 + 1
            dx = p*2+ len(M)*(2+p)
            dy = p*2+ len(M)*3 + 1
        else :
            a += 2
            b += 2
            d += 1
            dx += 2
            dy += 2
        it += 5
    return A

def format_right_in(M: List[Tuple[float, float]]) -> List[float]:
    b = [0 for _ in range(len(M) * 5)]
    return b



def format_left_eq(M: List[Tuple[float, float]], p: int) -> List[float]:
    mat = [[0 for _ in range(p*2+len(M)*(4+p))] for _ in range(len(M)*2)]
    nb_one = p * 2
    for i in range(len(M) * 2):
        mat[i][i+nb_one] = 1
    return mat


def format_right_eq(M):
    b_eq = []
    for a, b in M: 
        b_eq.append(a)
        b_eq.append(b)
    return b_eq

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


# For the moment, solve the optimal point between
# two other points given the coordinates of those
# points.
# TODO: use p and M parameters to generate the solution
# based on the user's gieven variables.
def solve(M, p):
    C    = format_equation(M, p)
    a_in = format_left_in(M, p)
    print(a_in)
    b_in = format_right_in(M)
    #print(C)
    a_eq = format_left_eq(M, p)
    b_eq = format_right_eq(M)
    
    res = linprog(C, A_ub=a_in, b_ub=b_in, A_eq=a_eq, b_eq=b_eq)
    print(res)

M = [(0, 50), (100, -25)]
p = 1
solve(M, p)


# def solve(M, p):
#     C=  [  0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ]
#     A=  [
#         # dA1
#             [ 0, 0, 0, 0, 0, 0, -1, 0, 1, 1, 0, 0 ],
#             [ 1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0 ],
#             [ -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0 ],
#             [ 0, 1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0 ],
#             [ 0, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0 ],
#         # dA2
#             [ 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1],
#             [ 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0],
#             [ -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0],
#             [ 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1],
#             [ 0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]

                # [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1]
                # [1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0]
                # [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0]
                # [0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1]
                #[0, -1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1]
#         ]

#     b=  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
#     A_eq = [
#         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
#         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ]
#     ]
#     b_eq = [ 10, 10, 20, 20 ]
#     bounds = [
#         (0, None), (0, None), (0, None), (0, None),
#         (0, None), (0, None), (0, None), (0, None),
#         (0, None), (0, None), (0, None), (0, None)
#     ]
#     res = linprog(C, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq)
#     print(res)

# m = p
# n = len(M)
# soit n le nombre d'acheteurs
# m le nombre de points relais
# c le nombre de contraintes par point acheteur (5)
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

# minimize z:        d1 + d2 + d3;

# # dA1
# subject to c11:    dx1 + dy1 <= d1;
# subject to c12:    x-a1 <= dx1;
# subject to c13:    a1-x <= dx1;
# subject to c14:    y-b1 <= dy1;
# subject to c15:    b1-y <= dy1;

# # dA2
# subject to c21:    dx2 + dy2 <= d2;
# subject to c22:    x-a2 <= dx2;
# subject to c23:    a2-x <= dx2;
# subject to c24:    y-b2 <= dy2;
# subject to c25:    b2-y <= dy2;

# subject to c106:   a1 >= 6;
# subject to c107:   a1 <= 6;
# subject to c108:   b1 <= 10;
# subject to c109:   b1 >= 10;

# subject to c96:   a2 >= 12;
# subject to c97:   a2 <= 12;
# subject to c98:   b2 <= 20;
# subject to c99:   b2 >= 20;
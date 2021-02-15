import numpy as np
from scipy.cluster.vq import kmeans, vq
from typing import Tuple, List
from scipy.optimize import linprog

def solve(M: List[Tuple[float, float]], p: int) -> List[Tuple[float, float]]:
    """
    Clusters the list of points M, loop over each cluster
    and apply the simplex solutions.
    """
    clusters = cluster(M, p)
    results = []
    for c in clusters:
        results.append(compute_simplex(c, 1))
    display_output(M, p, results)
    return results

def cluster(M: List[Tuple[float, float]], p: int) -> List[Tuple[float, float]]:
    """
    Regroups the nearest client positions in p clusters.
    In:     M=[(0, 50), (100, 25), (100, 40) (50, 85)], p=3
    Out:    [[(0, 50)], 
            [(100, 25), (100, 40)], 
            [50, 85]]
    """
    data = np.vstack(M)
    means, _ = kmeans(data, p)
    cluster_indexes, _ = vq(data, means)
    clusters = [[] for _ in range(p)]
    for i in range(len(cluster_indexes)):
        index = cluster_indexes[i]
        clusters[index].append((data[i][0], data[i][1]))
    return clusters

def compute_simplex(M: List[Tuple[float, float]], p: int) -> Tuple[float, float]:
    """
    Build all the needed matrices to apply the simplex method and 
    finally apply the algorithm using linprog().
    """
    C    = format_equation(M, p)
    a_in = format_left_in(M, p)
    b_in = format_right_in(M, p)
    a_eq = format_left_eq(M, p)
    b_eq = format_right_eq(M)
    res = linprog(C, A_ub=a_in, b_ub=b_in, A_eq=a_eq, b_eq=b_eq)
    # adjust 0f in nf for n decimals precision
    return (float("%.0f" % res.x[0]), float("%.0f" %res.x[1]))

def format_equation(M: List[Tuple[float, float]], p: int) -> List[float]:
    """
    Returns the equation C to minimize, built from the list of clients and
    the number of stations to consider.
    """
    C = [0 for _ in range(2 * p + 2 * len(M) + len(M) * p + 2 * p * len(M))]
    start = 2 * p + 2 * len(M)
    end = start + len(M) * p
    for i in range(start, end):
        C[i] = 1
    return C
    
def format_left_in(M: List[Tuple[float, float]], p: int) -> List[float]:
    """
    Returns the lhs of the inequation matrix, considering also the rhs variables
    for simplicity purpose.
    """
    A = [[0 for i in range(len(M) * (2 + 3 * p) + p * 2)] for _ in range(len(M) * 5 * p)]
    x = 0
    y = 1
    d = p * 2 + len(M) * 2
    a = p * 2
    b = p * 2 + 1
    dx = p * 2 + len(M) * (2 + p)
    dy = p * 2 + len(M) * (2 + p) + 1
    it = 0
    for i in range(0, len(M)*p):
        # constraint 1
        A[it][dx] = 1
        A[it][dy] = 1
        A[it][d] = -1
        # constraint 2
        A[it + 1][x] = 1
        A[it + 1][a] = -1
        A[it + 1][dx] = -1
        # constraint 3
        A[it + 2][x] = -1
        A[it + 2][a] = 1
        A[it + 2][dx] = -1
        # constraint 4
        A[it + 3][y] = 1
        A[it + 3][b] = -1
        A[it + 3][dy] = -1
        # constraint 5
        A[it + 4][y] = -1
        A[it + 4][b] = 1
        A[it + 4][dy] = -1
        # update indexes
        # consider the next (xi,yi) when the last element is reached
        if i % len(M) == len(M) - 1:
            x += 2
            y += 2
            d = p * 2 + len(M) * 2
            a = p * 2
            b = p * 2 + 1
        else :
            a += 2
            b += 2
            d += 1
        dx += 2
        dy += 2
        it += 5
    return A

def format_right_in(M: List[Tuple[float, float]], p: int) -> List[float]:
    """
    Returns the lhs of inequations matrix, which is full of zeros because
    we have substituted the values to the lhs of the inequation.
    """
    b = [0 for _ in range(len(M) * 5 * p)]
    return b



def format_left_eq(M: List[Tuple[float, float]], p: int) -> List[float]:
    """
    Returns the lhs of the equations matrix, which represents the variable
    names.
    """
    a_eq = [[0 for _ in range(p * 2 + len(M) * (2 + 3 * p))] for _ in range(len(M) * 2)]
    nb_one = p * 2
    for i in range(len(M) * 2):
        a_eq[i][i+nb_one] = 1
    return a_eq


def format_right_eq(M: List[Tuple[float, float]]) -> List[int]:
    """
    Returns the rhs of the equations matrix, which represents the variable
    values.
    """
    b_eq = []
    for a, b in M: 
        b_eq.append(a)
        b_eq.append(b)
    return b_eq

def display_output(
    M: List[Tuple[float, float]], 
    p: int, 
    results: List[Tuple[float, float]]):
    """
    Prining of the input data and algorithm solution.
    """
    print('Input:')
    print('\t M = ', M)
    print('\t p = {}\n'.format(p))
    print('Output:')
    for (x, y) in results:
        print('\t{}, {}'.format(x, y))
    print()

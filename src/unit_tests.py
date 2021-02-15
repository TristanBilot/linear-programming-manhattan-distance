#!/usr/bin/env python3

from manhattan import solve
import unittest

class ManhattanDistanceTests(unittest.TestCase):

    def test_M2_p1(self):
        M = [(0., 10.), (10., 20.)]
        p = 1
        sol = solve(M, p)
        self.assertEqual(sol[0], (5, 14))

    def test_M2_p2(self):
        M = [(0., 10.), (10., 20.)]
        p = 2
        sol = solve(M, p)
        self.assertTrue(sol.__contains__(M[0]))
        self.assertTrue(sol.__contains__(M[1]))

    def test_M5_p1(self):
        M = [(0., 10.), (10., 20.), (20., 30.), (30., 40.), (50., 60.)]
        p = 1
        sol = solve(M, p)
        self.assertEqual(sol, [(20, 30)])

    def test_huge_values(self):
        M = [(39434390., 2323232343.), (2323232., 34356565.), (42., 42.)]
        p = 2
        sol = solve(M, p)
        self.assertTrue(sol.__contains__((1340209, 15487478)))
        self.assertTrue(sol.__contains__((221976703, 572796955)))

    def test_hugesd_values(self):
        M = [(10., 20.), (15., 45.), (22., 19.), (33., 42.)]
        p = 2
        sol = solve(M, p)
        print(sol)
        
if __name__ == '__main__':
    unittest.main()
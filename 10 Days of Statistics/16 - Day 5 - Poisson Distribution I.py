# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

from math import factorial, exp

MEAN = float(input())
K = int(input())

POISSON = ((MEAN ** K) * exp(-MEAN)) / factorial(K)

print("%.3f" % POISSON)

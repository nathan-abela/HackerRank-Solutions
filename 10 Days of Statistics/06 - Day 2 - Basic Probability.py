# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-mcq-1/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python
# Multiple Choice Question - No code required but checked with code

# ========================
#         Solution
# ========================

from itertools import product
from fractions import Fraction

P = list(product([1, 2, 3, 4, 5, 6], repeat=2))

N = sum(1 for x in P if sum(x) <= 9)

print(Fraction(N, len(P)))

# >>> 5/6

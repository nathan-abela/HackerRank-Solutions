# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

from cmath import polar

z = complex(input())

print(*polar(z), sep='\n')

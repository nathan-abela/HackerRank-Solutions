# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/itertools-product/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*list(product(A, B)))

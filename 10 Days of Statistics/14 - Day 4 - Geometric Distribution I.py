# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

A, B = map(int, input().strip().split(' '))
C = int(input())

P = float(A/B)

RES = (1-P) ** (C-1) * P

print(round(RES, 3))

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import math

H = int(input())
B = int(input())
C = int(input())
INPUT = math.sqrt(B) * int(input())

print(round(0.5 * (1 + math.erf((H - (B * C)) / (INPUT * math.sqrt(2)))), 4))

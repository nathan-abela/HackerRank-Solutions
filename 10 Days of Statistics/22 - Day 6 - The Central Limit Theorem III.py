# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import math

SAMPLE = 100
M = 500
SD = 80
Z = 1.96
RNG = 0.95

print(round(-1.96 * (SD/math.sqrt(SAMPLE)) + M, 2))
print(round(1.96 * (SD/math.sqrt(SAMPLE)) + M, 2))

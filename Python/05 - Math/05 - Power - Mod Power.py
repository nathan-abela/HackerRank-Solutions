# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-power-mod-power/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import math

a = int(input())
b = int(input())
m = int(input())

c = math.pow(a, b)
d = c%m

print(int(c))
print(int(d))

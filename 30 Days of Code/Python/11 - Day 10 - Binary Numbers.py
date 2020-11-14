# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
DATA = bin(N)

MAXIMUM = 0
CURRENT = 0

for num in DATA:
    if num == '1':
        CURRENT = CURRENT + 1
    else:
        MAXIMUM = max(MAXIMUM, CURRENT)
        CURRENT = 0

print(max(MAXIMUM, CURRENT))

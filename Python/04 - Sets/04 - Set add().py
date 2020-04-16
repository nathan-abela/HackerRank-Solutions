# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-add/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

n = int(input())

NAMES = set([])

for i in range(n):
    NAMES.add(input())

print(len(NAMES))

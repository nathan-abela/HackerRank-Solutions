# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from collections import deque

D = deque()

for _ in range(int(input())):
    oper, val, *args = input().split() + ['']
    eval(f'D.{oper} ({val})')

print(*D)

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

A = set(input().split())
COUNT = 0
VALUE = 0

for i in range(int(input())):
    if A.issuperset(set(input().split())):
        COUNT += 1
    else:
        VALUE += 1
if VALUE != 0:
    print('False')
else:
    print('True')

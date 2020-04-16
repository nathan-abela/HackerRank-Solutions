# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

NEW_SET = SET_N.difference(SET_B)
print(len(NEW_SET))

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from collections import namedtuple

N, STUDENT = int(input()), namedtuple('Student', input())

print("{:.2f}".format(sum([int(STUDENT(*input().split()).MARKS) for _ in range(N)]) / N))

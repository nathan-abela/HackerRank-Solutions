# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

from itertools import combinations

N = int(input())
LETTERS = list(input().split(" "))
K = int(input())

TUPLES = list(combinations(LETTERS, K))
CONTAINS = [word for word in TUPLES if "a" in word]

print(len(CONTAINS)/len(TUPLES))

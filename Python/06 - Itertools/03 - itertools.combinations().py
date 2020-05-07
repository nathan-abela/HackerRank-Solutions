# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

from itertools import combinations

S, N = input().split()

for i in range(1, int(N)+1):
    for j in combinations(sorted(S), i):
        print(''.join(j))

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from collections import defaultdict

N, M = map(int, input().split())
D = defaultdict(list)

for i in range(1, N + 1):
    D[input()].append(str(i))
for i in range(M):
    print(' '.join(D[input()]) or -1)

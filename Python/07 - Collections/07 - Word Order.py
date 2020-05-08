# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/word-order/problem
# Difficulty: Medium
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

from collections import Counter

N = int(input())
LIST = []

for i in range(N):
    LIST.append(input().strip())

COUNT = Counter(LIST)

print(len(COUNT))
print(*COUNT.values())

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/most-commons/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

from collections import Counter

S = input()
S = sorted(S)

FREQUENCY = Counter(list(S))

for k, v in FREQUENCY.most_common(3):
    print(k, v)

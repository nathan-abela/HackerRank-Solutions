# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/compress-the-string/problem
# Difficulty: Medium
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from itertools import groupby

for k, c in groupby(input()):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

for _ in range(int(input())):
    try:
        a = re.compile(input())
        print("True")
    except Exception:
        print("False")

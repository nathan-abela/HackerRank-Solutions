# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-print/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())

for _ in range(1, N+1):
    print(_, end="")

# ========================
#       Explanation
# ========================

# Without the (end=""), every number would be printed on the next line

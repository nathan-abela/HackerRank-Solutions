# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

n = int(input())
s = list(map(int, input().split()))

for i in range(1, n + 1):
    print(s.index(i) + 1)

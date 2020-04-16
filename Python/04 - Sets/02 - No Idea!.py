# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/no-idea/problem
# Difficulty: Medium
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

N = input().split()
M = input().split()
A = set(input().split())
B = set(input().split())

COUNTER = 0

for i in M:
    if i in A:
        COUNTER += 1
    if i in B:
        COUNTER -= 1

print(COUNTER)

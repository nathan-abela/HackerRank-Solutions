# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

RESULT = []

for a in range(0, X + 1):
    for b in range(0, Y + 1):
        for c in range(0, Z + 1):
            if (a + b + c) != N:
                RESULT.append([a, b, c])

print(RESULT)

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-tutorial-permutations/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def permutation():
    n = input()
    values = list(map(int, input().split()))

    for i, n in enumerate(values):
        print(values[values[i] - 1])

permutation()

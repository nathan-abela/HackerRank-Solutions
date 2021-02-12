# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-involution/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def involution():
    n = input()
    values = list(map(int, input().split()))

    for i, n in enumerate(values):
        first = [values[values[i] - 1]][0]
        second = i + 1
        if first != second:
            print('NO')
            exit()
    print('YES')

involution()

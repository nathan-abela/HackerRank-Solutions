# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/exceptions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as z:
        print(f'Error Code: {z}')
    except ValueError as v:
        print(f'Error Code: {v}')

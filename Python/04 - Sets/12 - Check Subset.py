# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-check-subset/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

for i in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))

    b = int(input())
    set_b = set(map(int, input().split()))

    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")

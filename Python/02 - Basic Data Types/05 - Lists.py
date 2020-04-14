# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
ARRAY = []

while N != 0:
    A = input().split()

    if len(A) == 3:
        B = int(A[1])
        C = int(A[2])
    elif len(A) == 2:
        B = int(A[1])

    if A[0] == "insert":
        ARRAY.insert(B, C)
    elif A[0] == "print":
        print(ARRAY)
    elif A[0] == "remove":
        ARRAY.remove(B)
    elif A[0] == "append":
        ARRAY.append(B)
    elif A[0] == "sort":
        ARRAY.sort()
    elif A[0] == "pop":
        ARRAY.pop()
    elif A[0] == "reverse":
        ARRAY.reverse()
    N -= 1

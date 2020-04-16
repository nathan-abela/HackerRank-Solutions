# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

A = int(input())
SET_A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation = input().split()
    new_set = set(map(int, input().split()))
    eval('SET_A.{}({})'.format(operation[0], new_set))

print(sum(SET_A))

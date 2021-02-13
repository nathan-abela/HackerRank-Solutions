# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-key-spaces/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

num = (input())
e = int(input())

print(''.join([str((int(i)+e) % 10) for i in num]))

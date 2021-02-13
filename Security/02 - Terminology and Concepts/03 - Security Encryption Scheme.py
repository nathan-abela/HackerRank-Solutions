# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-encryption-scheme/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def get_fact(n):
    if (n == 1):
        return 1

    return n * get_fact(n-1)

n = int(input())

print(get_fact(n))

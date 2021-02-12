# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-bijective-functions/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

t = int(input())
s = list(map(int, input().split()))

if len(set(s)) == t:
    print("YES")
else:
    print("NO")

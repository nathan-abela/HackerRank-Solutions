# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

N, M = map(int, input().split())

for i in range(int(N/2)):
    string = ".|." * (2 * i + 1)
    x = string.center(M, '-')
    print(x)

print("WELCOME".center(M, '-'))

for i in reversed(range(int(N/2))):
    string = ".|." * (2 * i + 1)
    x = string.center(M, '-')
    print(x)

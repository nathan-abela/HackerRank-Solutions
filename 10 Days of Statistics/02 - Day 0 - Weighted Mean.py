# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

X = int(input())
ARRAY = list(map(int, input().split()))
WEIGHT = list(map(int, input().split()))
Y = 0

for i in range(X):
    Y += ARRAY[i]*WEIGHT[i]

print("{:.1f}".format(Y/sum(WEIGHT)))

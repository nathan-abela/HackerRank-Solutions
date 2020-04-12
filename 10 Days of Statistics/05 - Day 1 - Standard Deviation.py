# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-standard-deviation
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
X = list(map(int, input().strip().split(' ')))

MEAN = sum(X)/N
sum = 0

for i in range(N):
    sum += ((X[i]-MEAN)**2)/N

print(round(sum**0.5, 1))

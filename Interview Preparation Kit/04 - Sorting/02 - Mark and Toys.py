# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/mark-and-toys/problem
# Difficulty: Easy
# Max Score: 35
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    cost = 0
    toys = 0
    prices.sort()

    for j in range(0, n-1):
        if cost + prices[j] < k:
            cost += prices[j]
            toys += 1

    return toys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    PRICES = list(map(int, input().rstrip().split()))
    RESULT = maximumToys(PRICES, k)

    fptr.write(str(RESULT) + '\n')
    fptr.close()

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/greedy-florist/problem
# Difficulty: Medium
# Max Score: 35
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    sc = sorted(c, reverse=True)

    s = 0
    counter = 0
    additional = 0

    for c in sc:
        if counter == k:
            counter = 0
            additional += 1

        s += (additional + 1) * c

        counter += 1

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    MINIMUM_COST = getMinimumCost(k, c)

    fptr.write(str(MINIMUM_COST) + '\n')
    fptr.close()

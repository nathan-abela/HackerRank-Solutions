# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the rotLeft function below.
def rotLeft(a, d):
    size = len(a)

    if size < d:
        d = size % d
    return a[d:size] + a[0:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    RESULT = rotLeft(a, d)
    fptr.write(' '.join(map(str, RESULT)))
    fptr.write('\n')
    fptr.close()

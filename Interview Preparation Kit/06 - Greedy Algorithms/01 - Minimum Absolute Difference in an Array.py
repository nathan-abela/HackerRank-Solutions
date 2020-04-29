# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
# Difficulty: Easy
# Max Score: 15
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(array):
    array.sort()
    diff = abs(array[0] - array[1])
    for i in range(1, len(array)-1):
        if abs(array[i]-array[i+1]) < diff:
            diff = abs(array[i]-array[i+1])
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ARR = list(map(int, input().rstrip().split()))
    RESULT = minimumAbsoluteDifference(ARR)

    fptr.write(str(RESULT) + '\n')
    fptr.close()

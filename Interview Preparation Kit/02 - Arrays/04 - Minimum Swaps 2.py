# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    i = swap = 0

    while i < len(arr):

        while arr[i] != arr[arr[i]-1]:

            temp = arr[i]

            arr[i] = arr[temp-1]

            arr[temp-1] = temp
            swap += 1
        i += 1
    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ARRAY = list(map(int, input().rstrip().split()))

    RESULT = minimumSwaps(ARRAY)
    fptr.write(str(RESULT) + '\n')
    fptr.close()

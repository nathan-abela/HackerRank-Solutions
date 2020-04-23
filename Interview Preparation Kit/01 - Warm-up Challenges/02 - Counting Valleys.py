# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/counting-valleys/problem
# Difficulty: Easy
# Max Score: 15
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    num_valley = 0

    for i in s:
        if i == "U":
            level = level+1
        if i == "D":
            level = level -1
        if(level == 0 and i == "U"):
            num_valley += 1
    return num_valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()

    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()

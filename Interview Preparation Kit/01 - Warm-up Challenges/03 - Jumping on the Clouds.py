# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c) - 1:
        if (i + 2) < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()

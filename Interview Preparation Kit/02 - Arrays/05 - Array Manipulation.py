# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/crush/problem
# Difficulty: Hard
# Max Score: 60
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    max_value = 0
    total_sum = 0

    for query in queries:
        l = query[0]
        h = query[1]
        val = query[2]
        arr[l-1] = arr[l-1] + val
        arr[h] = arr[h]-val
    for value in arr:
        total_sum = total_sum + value
        max_value = max(max_value, total_sum)
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    QUERIES = []
    for _ in range(m):
        QUERIES.append(list(map(int, input().rstrip().split())))

    RESULT = arrayManipulation(n, QUERIES)
    fptr.write(str(RESULT) + '\n')
    fptr.close()

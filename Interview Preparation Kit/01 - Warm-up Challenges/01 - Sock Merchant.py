# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/sock-merchant/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    visited = []
    for i in range(n):
        if ar[i] not in visited:
            visited.append(ar[i])
            count = 1
            for j in range(i + 1, n):
                if ar[i] == ar[j]:
                    count += 1
            pairs += int(count/2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()

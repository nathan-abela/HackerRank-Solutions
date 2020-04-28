# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/alternating-characters/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')

    fptr.close()

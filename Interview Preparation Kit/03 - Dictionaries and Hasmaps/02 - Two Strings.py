# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/two-strings/problem
# Difficulty: Easy
# Max Score: 25
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)
        fptr.write(result + '\n')

    fptr.close()

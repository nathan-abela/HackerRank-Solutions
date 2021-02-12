# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/security-tutorial-functions/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import os

def calculate(x):
    return x % 11

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input())
    result = calculate(x)

    fptr.write(str(result) + '\n')
    fptr.close()

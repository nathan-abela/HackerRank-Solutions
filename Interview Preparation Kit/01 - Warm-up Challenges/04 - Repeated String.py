# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/repeated-string/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_1 = n//len(s) * s.count('a')
    remained_string = n%len(s)
    count_2 = s[:remained_string].count('a')
    return count_1 + count_2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()

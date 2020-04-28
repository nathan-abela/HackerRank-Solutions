# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# Difficulty: Easy
# Max Score: 25
# Language: Python

# ========================
#         Solution
# ========================

import os
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    difference_a = count_a - count_b
    difference_b = count_b - count_a

    return sum(difference_a.values()) + sum(difference_b.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()

    result = makeAnagram(a, b)
    fptr.write(str(result) + '\n')

    fptr.close()

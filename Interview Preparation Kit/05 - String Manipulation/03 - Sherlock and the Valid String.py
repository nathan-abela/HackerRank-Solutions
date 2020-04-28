# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# Difficulty: Medium
# Max Score: 35
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the isValid function below.
def isValid(s):
    frequency = {}

    # Set frequencies
    for char in s:
        frequency.setdefault(char, 0)
        frequency[char] += 1

    values = list(frequency.values())

    # Not important which number is used, in this case, first will be used
    first = values[0]
    accumulated_difference = 0

    for _ in values:
        # Difference is taken into consideration -> abs()
        diff = abs(_ - first)

        # If the value is 1, without taking into consideration the difference, it is counted as 1
        accumulated_difference += diff if _ != 1 else 1

        # Stops if the the difference is already more than 1
        if accumulated_difference > 1:
            return "NO"

    return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    RESULT = isValid(s)
    fptr.write(RESULT + '\n')

    fptr.close()

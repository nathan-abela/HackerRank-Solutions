# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/2d-array/problem
# Difficulty: Easy
# Max Score: 15
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    new_array = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_array.append(arr[i][j:j+3])
    second_array = []
    for i in range(len(new_array)-13):
        if len(new_array[i]) == 3:
            temp = []
            temp.extend(new_array[i])
            temp.extend(new_array[i+12])
            temp.extend(new_array[i+6][1:2])
            second_array.append(sum(temp))
    return max(second_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ARRAY = []

    for _ in range(6):
        ARRAY.append(list(map(int, input().rstrip().split())))

    RESULT = hourglassSum(ARRAY)
    fptr.write(str(RESULT) + '\n')
    fptr.close()

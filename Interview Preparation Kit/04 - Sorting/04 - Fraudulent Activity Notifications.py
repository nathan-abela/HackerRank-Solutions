# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    count_array = [0] * 201

    for i in range(d):
        count_array[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        if expenditure[i] >= getMedianVal(count_array, d) * 2:
            count += 1
        count_array[expenditure[i - d]] -= 1
        count_array[expenditure[i]] += 1

    return count

def getMedianVal(count_arr, d):
    is_length_even = d % 2 == 0
    total_count = 0

    for i, count in enumerate(count_arr):
        total_count += count

        if is_length_even:
            if total_count == d // 2:
                for j in range(i + 1, len(count_arr)):
                    if count_arr[j] > 0:
                        return (i + j) / 2
            elif total_count > d // 2:
                return i
        else:
            if total_count >= d // 2 + 1:
                return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    EXPENDITURE = list(map(int, input().rstrip().split()))
    RESULT = activityNotifications(EXPENDITURE, d)

    fptr.write(str(RESULT) + '\n')
    fptr.close()

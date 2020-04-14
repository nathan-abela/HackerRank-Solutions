# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
ARRAY = map(int, input().split())
MY_LIST = list(ARRAY)

MY_LIST.sort()
HIGHEST_NUMBER = max(MY_LIST)

for i in range(len(MY_LIST)-1, -1, -1):
    if MY_LIST[i] < HIGHEST_NUMBER:
        break

print(MY_LIST[i])

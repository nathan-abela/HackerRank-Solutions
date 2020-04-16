# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

N = input()
ROOM_LIST = input().split()
ROOM_SET = set(ROOM_LIST)

for ele in list(ROOM_SET):
    ROOM_LIST.remove(ele)

CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
print(CAPTAIN_ROOM_NUM)

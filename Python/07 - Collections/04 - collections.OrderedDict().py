# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

from collections import OrderedDict

A_LIST = OrderedDict()

N = int(input())

for i in range(N):
    inp = input()

    if type(inp) != int:
        isplit = inp.split()
        cost = isplit[-1]
        item = isplit[:-1]
        item = " ".join(item)
        cost = "".join(cost)
        cost = int(cost)

        if item in A_LIST:
            current = A_LIST[item]
            current += cost
            A_LIST[item] = current
        else:
            A_LIST[item] = cost


for key, value in A_LIST.items():
    print(key, value)

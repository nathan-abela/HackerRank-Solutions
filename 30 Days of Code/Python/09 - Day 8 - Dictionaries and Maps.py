# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

n = int(input())
d = {}

for i in range(n):
    x = input().split()
    d[x[0]] = x[1]

while True:
    try:
        NAME = input()
        if NAME in d:
            print(NAME, "=", d[NAME], sep="")
        else: print("Not found")
    except:
        break

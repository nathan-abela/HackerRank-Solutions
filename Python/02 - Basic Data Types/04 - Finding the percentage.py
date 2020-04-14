# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
STUDENT_MARKS = {}

for line in range(N):
    info = input().split(" ")
    grades = list(map(float, info[1:]))
    STUDENT_MARKS[info[0]] = sum(grades) / float(len(grades))

print("%.2f" % round(STUDENT_MARKS[input()], 2))

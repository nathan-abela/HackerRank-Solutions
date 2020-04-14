# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

STUDENTS = []
SECOND_LOWEST_GRADES = []
GRADES = set()

for _ in range(int(input())):
    name = input()
    grade = float(input())
    STUDENTS.append([name, grade])
    GRADES.add(grade)

SECOND_LOWEST = sorted(GRADES)[1]

for name, grade in STUDENTS:
    if grade == SECOND_LOWEST:
        SECOND_LOWEST_GRADES.append(name)

for name in sorted(SECOND_LOWEST_GRADES):
    print(name, end='\n')

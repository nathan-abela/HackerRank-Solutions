# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-nested-logic/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

DAY_1, MONTH_1, YEAR_1 = map(int, input().split())
DAY_2, MONTH_2, YEAR_2 = map(int, input().split())

def date():
    if YEAR_1 > YEAR_2:
        return 10000
    if YEAR_1 == YEAR_2:
        if MONTH_1 > MONTH_2:
            return (MONTH_1-MONTH_2) * 500
        if MONTH_1 == MONTH_2 and DAY_1 > DAY_2:
            return (DAY_1-DAY_2)*15
    return 0

RESULT = date()
print(RESULT)

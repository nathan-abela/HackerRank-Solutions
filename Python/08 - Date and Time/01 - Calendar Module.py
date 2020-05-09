# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/calendar-module/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import calendar

MONTH, DAY, YEAR = map(int, input().split())

print(calendar.day_name[calendar.weekday(YEAR, MONTH, DAY)].upper())

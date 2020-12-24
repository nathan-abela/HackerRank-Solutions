# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^\d+[A-Z]+[a-z]+$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d+
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── + - Denotes the above expression for 1 or unlimited times, same as {1,}
# ├── [A-Z]+
# │   ├── A-Z - Denotes a single character in the range of A and Z
# │   └── + - Denotes the above expression for 1 or unlimited times, same as {1,}
# ├── [a-z]+
# │   ├── a-z - Denotes a single character in the range of a and z
# │   └── + - Denotes the above expression for 1 or unlimited times, same as {1,}
# └── $
#     └── Denotes the end of the line

# Example: 1Qa
# Example: 0Aa

print(str(bool(re.search(regex_pattern, input()))).lower())

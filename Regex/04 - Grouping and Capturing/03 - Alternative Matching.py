# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/alternative-matching/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^(Mr?s|[MDE]r)\.[a-zA-Z]+$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── (Mr?s|[MDE]r)
# │   ├── Mr?s
# │   │   ├── M - Denotes an 'M' character
# │   │   ├── r - Denotes an 'r' character
# │   │   ├── ? - Denotes the above expression for 0 and 1 times
# │   │   └── s - Denotes an 's' character
# │   ├── | - Denotes a boolean OR operator
# │   ├── [MDE] - Denotes any single character included in the list 'MDE'
# │   └── r - Denotes an 'r' character
# ├── \.
# │   └── Denotes a '.' character
# ├── [a-zA-Z]+
# │   ├── a-z - Denotes a single character in the range of a and z
# │   ├── A-Z - Denotes a single character in the range of A and Z
# │   └── + - Denotes the above expression for 1 or unlimited times, same as {1,}
# └── $
#     └── Denotes the end of the line

# Example: Mr.Robot
# Example: Mr.Bean

print(str(bool(re.search(regex_pattern, input()))).lower())

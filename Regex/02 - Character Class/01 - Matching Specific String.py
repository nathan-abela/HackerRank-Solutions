# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-specific-characters/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^[1-3][0-2][xs0][30Aa][xsu][.,]$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── [1-3]
# │   └── Denotes a single character in the range of 1 and 3
# ├── [0-2]
# │   └── Denotes a single character in the range of 0 and 2
# ├── [xs0]
# │   └── Denotes a single character from the list 'xs0'
# ├── [30Aa]
# │   └── Denotes a single character from the list '30Aa'
# ├── [xsu]
# │    └── Denotes a single character from the list 'xsu'
# ├── [.,]
# │    └── Denotes a single character from the list '.,'
# └── $
#     └── Denotes the end of the line

# Example: 1203x.

print(str(bool(re.search(regex_pattern, input()))).lower())

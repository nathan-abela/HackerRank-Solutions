# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-start-end/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^\d\w{4}\.$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d
# │   └── Denotes a digit (equal to [0-9])
# ├── \w{4}
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   └── {4} - Denotes the above expression for 4 times
# ├── \.
# │   └── Denotes a '.' character
# └── $
#     └── Denotes the end of the line

# Example: 0qwer.

print(str(bool(re.search(regex_pattern, input()))).lower())

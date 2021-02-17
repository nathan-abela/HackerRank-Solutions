# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/positive-lookahead/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'o(?=oo)'

# Regex Pattern:
# .
# ├── o
# │   └── Denotes an 'o' character
# └── (?=oo)
#     ├── ?= - Denotes a positive lookahead, looks for 'o' but matches only if followed by 'oo'
#     └── oo - Denotes a 'oo' character

# Example: gooooo
# Example: oooooogooo

Test_String = input()

match = re.findall(regex_pattern, Test_String)

print("Number of matches :", len(match))

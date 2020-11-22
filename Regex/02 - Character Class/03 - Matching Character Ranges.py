# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-range-of-characters/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── [a-z]
# │   └── Denotes a single character in the range of a and z
# ├── [1-9]
# │   └── Denotes a single character in the range of 1 and 9
# ├── [^a-z]
# │    └── Denotes any single character not included in the list 'a-z'
# ├── [^A-Z]
# │    └── Denotes any single character not included in the list 'A-Z'
# └── [A-Z]
#     └── Denotes a single character in the range of A and Z

# Example: h4CkR
# Example: a1AaA

print(str(bool(re.search(regex_pattern, input()))).lower())

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-ending-items/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^[a-zA-Z]*s$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── [a-zA-Z]*
# │   ├── a-z - Denotes a single character in the range of a and z
# │   ├── A-Z - Denotes a single character in the range of A and Z
# │   └── * - Denotes the above expression for 0 or unlimited times, same as {0,}
# ├── s
# │   └── Denotes a 's' character
# └── $
#     └── Denotes the end of the line

# Example: Kites
# Example: 1ess

print(str(bool(re.search(regex_pattern, input()))).lower())

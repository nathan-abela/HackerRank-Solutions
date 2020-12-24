# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^\d{1,2}[a-zA-z]{3,}[.]{0,3}$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d{1,2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {1,2}- Denotes the above expression for 1 or 2 times
# ├── [a-zA-z]{3,}
# │   ├── a-z - Denotes a single character in the range of a and z
# │   ├── A-Z - Denotes a single character in the range of A and Z
# │   └── {3,} - Denotes the above expression for 3 or unlimited times
# ├── [.]{0,3}
# │   ├── [.] - Denotes a '.' character
# │   └── {0,3} - Denotes the above expression for 0 up to 3 times
# └── $
#     └── Denotes the end of the line

# Example: 0aAa.
# Example: 3threeormorealphabets.

print(str(bool(re.search(regex_pattern, input()))).lower())

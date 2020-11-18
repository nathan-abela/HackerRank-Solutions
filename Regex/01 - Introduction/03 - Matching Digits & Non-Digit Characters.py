# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^\d{2}.\d{2}.\d{4}'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d{2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2} - Denotes the above expression for 2 times
# ├── .
# │   └── Denotes any characters
# ├── \d{2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2} - Denotes the above expression for 2 times
# ├── .
# │   └── Denotes any characters
# └── \d{4}
#     ├── \d - Denotes a digit (equal to [0-9])
#     └── {4} - Denotes the above expression for 4 times

# Example: 18-11-2020

print(str(bool(re.search(regex_pattern, input()))).lower())

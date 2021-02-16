# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/branch-reset-groups/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^\d{2}(-?)(\d{2}\1){2}\d{2}$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \d{2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2} - Denotes the above expression for 2 times
# ├── (-?)
# │   ├── - - Denotes a '-' character
# │   └── ? - Denotes the above expression for 0 and 1 times
# ├── (\d{2}\1){2}
# │   ├── (\d{2}\1)
# │   │   ├── \d - Denotes a digit (equal to [0-9])
# │   │   ├── {2} - Denotes the above expression for 2 times
# │   │   └── \1 - Denotes the first matching group
# │   └── {2} - Denotes the above expression for 2 times
# ├── \d{2}
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   └── {2} - Denotes the above expression for 2 times
# └── $
#     └── Denotes the end of the line

# Example: 12-34-56-78
# Example: 12345678

print(str(bool(re.search(regex_pattern, input()))).lower())

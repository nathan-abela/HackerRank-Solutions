# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^(...\.){3}...$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── (...\.){3}
# │   ├── ... - Denotes any 3 characters
# │   ├── \. - Denotes a '.' character
# │   └── {3} - Denotes the above expression for 3 times
# ├── ...
# │   └── Denotes any 3 characters
# └── $
#     └── Denotes the end of the line

# Example: 123.456.abc.def
# Example: ABC.BAC.CAB.ACB

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

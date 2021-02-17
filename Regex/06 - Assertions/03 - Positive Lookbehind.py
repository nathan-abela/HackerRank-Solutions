# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/positive-lookbehind/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'(?<=[13579])\d'

# Regex Pattern:
# .
# ├── (?<=[13579])
# │   ├── ?<= - Denotes a positive lookbehind
# │   ├── [13579] - Denotes any single character included in the list '13579'
# │   └── Matches \d, but only if there’s [13579] before it
# └── \d
#     └── Denotes a digit (equal to [0-9])

# Example: 123Go!
# Example: 11111

Test_String = input()

match = re.findall(regex_pattern, Test_String)

print("Number of matches :", len(match))

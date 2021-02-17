# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/negative-lookahead/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'(.)(?!\1)'

# Regex Pattern:
# .
# ├── (.)
# │   └── Denotes any character
# └── (?!\1)
#     ├── ?! - Denotes a negative lookahead
#     ├── \1 - Denotes the first matching group
#     └── Searches for 'any character' but only if NOT followed by 'first matching group'

# Example: gooooo
# Example: goluo

Test_String = input()

match = re.findall(regex_pattern, Test_String)

print("Number of matches :", len(match))

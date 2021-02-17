# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/negative-lookbehind/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'(?<![aeiouAEIOU]).'

# Regex Pattern:
# .
# ├── (?<![aeiouAEIOU])
# │   ├── ?<! - Denotes a negative lookbehind
# │   ├── [aeiouAEIOU] - Denotes any single character included in the list 'aeiouAEIOU'
# │   └── Matches 'any character', but only if there’s no [aeiouAEIOU] before it
# └── .
#     └── Denotes any character

# Example: 1o1s
# Example: thisisavowel

Test_String = input()

match = re.findall(regex_pattern, Test_String)

print("Number of matches :", len(match))

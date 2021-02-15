# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-word-boundaries/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

# Regex Pattern:
# .
# ├── \b
# │   └── Denotes the start of a word boundary
# ├── [aeiouAEIOU]
# │   └── Denotes any single character included in the list 'aeiouAEIOU'
# ├── [a-zA-Z]*
# │   ├── a-zA-Z - Denotes any single character  included in the list 'a-zA-Z'
# │   └── * - Denotes the above expression for 0 or unlimited times, same as {0,}
# └── \b
#     └── Denotes the end of the word boundary

# Example: abc

print(str(bool(re.search(regex_pattern, input()))).lower())

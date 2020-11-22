# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/excluding-specific-characters/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── \D
# │   └── Denotes any character that is not a digit (equal to [^0-9])
# ├── [^aeiou]
# │   └── Denotes any single character not included in the list 'aeiou'
# ├── [^bcDF]
# │   └── Denotes any single character not included in the list 'bcDF'
# ├── \S
# │   └── Denotes any non-whitespace character (equal to [^\r\n\t\f\v ])
# ├── [^AEIOU]
# │   └── Denotes any single character not included in the list 'AEIOU'
# ├── [^.,]
# │    └── Denotes any single character not included in the list '.,'
# └── $
#     └── Denotes the end of the line

# Example: think?
# Example: fluff!

print(str(bool(re.search(regex_pattern, input()))).lower())

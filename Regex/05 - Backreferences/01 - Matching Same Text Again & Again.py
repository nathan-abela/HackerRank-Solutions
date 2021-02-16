# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-same-text-again-again/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aieouAEIOU]\S)\1$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── ([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aieouAEIOU]\S)
# │   ├── [a-z]
# │   │   └── Denotes a single character in the range of a and z
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   ├── \s - Denotes any whitespace character (equal to [\r\n\t\f\v ])
# │   ├── \W - Denotes any non-word character (equal to [^a-zA-Z0-9_])
# │   ├── \d - Denotes a digit (equal to [0-9])
# │   ├── \D - Denotes any character that is not a digit (equal to [^0-9])
# │   ├── [A-Z] - Denotes a single character in the range of A and Z
# │   ├── [a-zA-Z]
# │   │   ├── a-z - Denotes a single character in the range of a and z
# │   │   └── A-Z - Denotes a single character in the range of A and Z
# │   ├── [aieouAEIOU] - Denotes any single character included in the list 'aieouAEIOU'
# │   └── \S - Denotes any non-whitespace character (equal to [^\r\n\t\f\v ])
# ├── \1
# │   └── Denotes the first matching group
# └── $
#     └── Denotes the end of the line

# Example: ab #1?AZa$ab #1?AZa$

print(str(bool(re.search(regex_pattern, input()))).lower())

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-x-repetitions/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'^[a-zA-Z24680]{40}[13579\s]{5}$'

# Regex Pattern:
# .
# ├── ^
# │   └── Denotes the start of the line
# ├── [a-zA-Z24680]{40}
# │   ├── a-z - Denotes a single character in the range of a and z
# │   ├── A-Z - Denotes a single character in the range of A and Z
# │   ├── 24680 - Denotes any single character included in the list '24680'
# │   └── {40} - Denotes the above expression for 40 times
# ├── [13579\s]{5}
# │   ├── 13579 - Denotes any single character included in the list '13579'
# │   ├── \s - Denotes any non-whitespace character (equal to [^\r\n\t\f\v ])
# │   └── {5} - Denotes the above expression for 5 times
# └── $
#     └── Denotes the end of the line

# Example: 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57

print(str(bool(re.search(regex_pattern, input()))).lower())

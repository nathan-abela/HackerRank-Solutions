# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'(\S{2}\s){2}\S{2}'

# Regex Pattern:
# .
# ├── (\S{2}\s){2}
# │   ├── \S{2} - Denotes any non-whitespace character (equal to [^\r\n\t\f\v ]) for 2 times
# │   ├── \s - Denotes any whitespace character (equal to [\r\n\t\f\v ])
# │   └── {2} - Denotes the above expression for 2 times
# └── \S{2}
#     ├── \S - Denotes any non-whitespace character (equal to [^\r\n\t\f\v ]) for 2 times
#     └── {2} - Denotes the above expression twice

# Example: 18 11 20

print(str(bool(re.search(regex_pattern, input()))).lower())

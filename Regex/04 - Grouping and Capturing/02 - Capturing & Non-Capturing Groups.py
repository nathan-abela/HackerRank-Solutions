# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/capturing-non-capturing-groups/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'(ok){3,}'

# Regex Pattern:
# .
# └── (ok){3,}
#     ├── (ok) - Denotes the 'ok' string
#     └── {3,} - Denotes the above expression for 3 or more times

# Example: okokok

print(str(bool(re.search(regex_pattern, input()))).lower())

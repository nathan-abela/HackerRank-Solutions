# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-specific-string/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'hackerrank'

# Regex Pattern:
# hackerrank - Denotes the 'hackerrank' string

# Example: hackerrank

test_string = input()

match = re.findall(regex_pattern, test_string)

print("Number of matches :", len(match))

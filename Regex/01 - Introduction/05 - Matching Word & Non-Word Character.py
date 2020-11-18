# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matching-word-non-word/problem
# Difficulty: Easy
# Max Score: 5
# Language: Python

# ========================
#         Solution
# ========================

import re

regex_pattern = r'\w{3}\W\w{10}\W\w{3}'

# Regex Pattern:
# .
# ├── \w{3}
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   └── {3} - Denotes the above expression for 3 times
# ├── \W
# │   └── Denotes any non-word character (equal to [^a-zA-Z0-9_])
# ├── \w{10}
# │   ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
# │   └── {10} - Denotes the above expression for 10 times
# ├── \W
# │   └── Denotes any non-word character (equal to [^a-zA-Z0-9_])
# └── \w{3}
#     ├── \w - Denotes a word character (equal to [a-zA-Z0-9_])
#     └── {3} - Denotes the above expression for 3 times

# Example: www.hackerrank.com
# Example: abc.defghijklm.nop

print(str(bool(re.search(regex_pattern, input()))).lower())

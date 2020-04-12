# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-mcq-3/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python
# Multiple Choice Question - No code required but checked with code

# ========================
#         Solution
# ========================

import itertools
from fractions import Fraction
from collections import Counter

# Let r = 1 and black = 0
# Bag X
X = list(Counter({1:4, 0:3}).elements())

# Bag Y 
Y = list(Counter({1:5, 0:4}).elements())

# Bag z
Z = list(Counter({1:4, 0:4}).elements())

# Sample space / total number of outcomes
TOTAL_SAMPLES = list(itertools.product(X, Y, Z))

# Total number of outcomes
TOTAL_SAMPLES_SIZE = len(TOTAL_SAMPLES)

# Total number of favourable outcomes
FAVOURABLE_OUTCOMES_SIZE = sum([sum(i) == 2 for i in list(itertools.product(X, Y, Z))])

# Probability as a fraction
print(Fraction(FAVOURABLE_OUTCOMES_SIZE,TOTAL_SAMPLES_SIZE))

# >>> 17/42

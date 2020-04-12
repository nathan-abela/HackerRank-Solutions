# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-mcq-6/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python
# Multiple Choice Question - No code required but checked with code

# ========================
#         Solution
# ========================

from itertools import permutations
from fractions import Fraction

# 1 for Red Marbles
# 0 for Blue Marbles
RED_MARBLES = [1, 1, 1]
BLUE_MARBLES = [0, 0, 0, 0]

# All combinations, excluded first blue
FIRST_DRAW = list(filter(lambda m: m[0] == 1, permutations(RED_MARBLES + BLUE_MARBLES, 2)))

# All combinations with second blue
MARBLES_REMAINING = list(filter(lambda m: m[1] == 0, FIRST_DRAW))

# Result is 2/3
print(Fraction(len(MARBLES_REMAINING), len(FIRST_DRAW)))

# ========================
#       Explanation
# ========================

# A bag contains 3 red marbles and 4 blue marbles
# After drawing a red marble, the bag has now 2 red and 4 blue marbles (total of 6 marbles)
# Therefore, the probability of getting a blue marble is 4/6, simplified to 2/3

# >>> 2/3

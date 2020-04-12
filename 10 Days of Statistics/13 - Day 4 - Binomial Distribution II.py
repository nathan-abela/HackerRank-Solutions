# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import math

P = 0.12
ANS_1 = 0

for i in range(0, 3):
    ANS_1 += math.factorial(10)/math.factorial(i)/math.factorial(10-i) * P**i * (1-P)**(10-i)
    if i == 1:
        ANS_2 = 1 - ANS_1

print(round(ANS_1, 3))
print(round(ANS_2, 3))

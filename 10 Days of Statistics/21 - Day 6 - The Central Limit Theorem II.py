# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import math

TICKETS = 250
STUDENTS = 100
MEAN = 2.4
SD = 2

MU = STUDENTS * MEAN
S = math.sqrt(100)*SD

def normal_distribution(x, mu, sd):
    '''Function to calculate the distribution'''
    return 1/2*(1+math.erf((x-mu)/(sd*math.sqrt(2))))

print(round(normal_distribution(x=TICKETS, mu=MU, sd=S), 4))

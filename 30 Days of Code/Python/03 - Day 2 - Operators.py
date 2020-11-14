# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-operators/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def solve(meal_cost, tip_percent, tax_percent):
    '''Function to calculate the total cost'''
    tax = meal_cost* tip_percent/100 + meal_cost* tax_percent/100
    total = meal_cost + tax
    print(round(total))

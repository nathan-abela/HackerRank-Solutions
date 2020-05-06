# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a**b)+(c**d))

# ========================
#       Explanation
# ========================

# ** -> Exponentiation, example, (2 ** 3) is the same as 2*2*2
# ** is faster than math.pow() as it won’t have the overhead of a function call

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-more-exceptions/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

class Calculator:
    def power(self, n, p):
        '''Checks whether n or p are negative'''
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p

myCalculator = Calculator()
T = int(input())

for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

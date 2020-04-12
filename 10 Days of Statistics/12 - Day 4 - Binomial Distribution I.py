# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def factorial(N):
    '''Function to calculate N factorial'''
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)

def combination(N, X):
    '''Function to calculate the combination of N and X'''
    result = factorial(N) / (factorial(N - X) * factorial(X))
    return result

def binomial(X, N, P):
    '''Function to determine the binomial of X, N, and P'''
    Q = 1 - P
    result = combination(N, X) * (P**X) * (Q**(N - X))
    return result

if __name__ == '__main__':
    L, R = list(map(float, input().split()))
    ODDS = L / R
    TOTAL = list()
    for i in range(3, 7):
        TOTAL.append(binomial(i, 6, ODDS / (1 + ODDS)))
    print(round(sum(TOTAL), 3))

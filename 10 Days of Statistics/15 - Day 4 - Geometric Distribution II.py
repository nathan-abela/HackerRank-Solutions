# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def geometric_prob(P, X):
    '''Function to calculate the geometric probability'''
    G = (1-P)**(X-1) * P
    return G

NUMBERATOR, DENOMINATOR = map(float, input().split())
X = int(input())
P = NUMBERATOR/DENOMINATOR
G = 0

for i in range(1, 6): # i = 1, 2, 3, 4, 5
    G += geometric_prob(P, i)

print("%.3f" %G)

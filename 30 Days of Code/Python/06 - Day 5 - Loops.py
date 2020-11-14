# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-loops/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    n = int(input())

    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)

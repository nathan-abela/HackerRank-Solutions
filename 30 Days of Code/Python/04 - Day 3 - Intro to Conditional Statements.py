# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-conditional-statements/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    N = int(input())

    if N%2 != 0 or ((N > 5 and N < 21) and N%2 == 0):
        print("Weird")
    else:
        print("Not Weird")

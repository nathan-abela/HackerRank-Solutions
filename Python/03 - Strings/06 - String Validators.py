# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/string-validators/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    s = input()

    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))

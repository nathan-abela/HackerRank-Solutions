# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def print_formatted(number):
    '''Prints number in decinmal, ocal, hexadecimal, and binary'''
    for i in range(1, number + 1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

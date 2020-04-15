# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/text-wrap/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import textwrap # Solution made without using the required library

def wrap(string, max_width):
    '''Wraps the string into a paragraph of width w'''
    string = [c for c in string]

    for i in range(max_width, len(string) + max_width, max_width+1):
        string.insert(i, '\n')
    return ("").join(string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

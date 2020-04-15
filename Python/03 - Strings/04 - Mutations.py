# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-mutations/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def mutate_string(string, position, character):
    '''Changes a character at a given index'''
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# ========================
#        Explanation
# ========================

# The : (colon) is to slice-out sub-parts in sequences, example, [1:] is "1 to end"

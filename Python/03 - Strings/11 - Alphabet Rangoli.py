# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

def print_rangoli(size):
    '''Prints Rangoli Design'''
    width = size*4-3
    string = ''

    for i in range(1, size+1):
        for j in range(0, i):
            string += chr(96+size-j)
            if len(string) < width:
                string += '-'
        for k in range(i-1, 0, -1):
            string += chr(97+size-k)
            if len(string) < width:
                string += '-'
        print(string.center(width, '-'))
        string = ''

    for i in range(size-1, 0, -1):
        string = ''
        for j in range(0, i):
            string += chr(96+size-j)
            if len(string) < width:
                string += '-'
        for k in range(i-1, 0, -1):
            string += chr(97+size-k)
            if len(string) < width:
                string += '-'
        print(string.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

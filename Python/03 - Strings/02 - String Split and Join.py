# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def split_and_join(line):
    '''Converts 'space' to '-' '''
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

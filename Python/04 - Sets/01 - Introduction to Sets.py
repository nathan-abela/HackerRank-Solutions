# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

def average(array):
    '''Calculates the average of the array'''
    s = set(arr)
    return float(sum(s)) / len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

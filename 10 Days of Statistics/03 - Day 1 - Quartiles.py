# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-quartiles/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
ARRAY = sorted(map(int, input().rstrip().split()))

def median(n, array):
    '''Function to calculate the median'''

    if n % 2 == 0:
        ind1 = n//2
        ind2 = ind1 - 1
        return (array[ind1] + array[ind2]) // 2
    else:
        return array[n//2]

MEDIAN_L = median(N//2, ARRAY[0:N//2])
MEDIAN_X = median(N, ARRAY)
MEDIAN_U = median(N//2, ARRAY[(N+1)//2:])

print(MEDIAN_L)
print(MEDIAN_X)
print(MEDIAN_U)

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                a[i] = a[i]+a[j]
                a[j] = a[i]-a[j]
                a[i] = a[i] - a[j]
                count += 1

    print('Array is sorted in {} swaps.'.format(count))
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
    countSwaps(a)

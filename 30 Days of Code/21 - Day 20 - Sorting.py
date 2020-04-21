# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-sorting/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
NUM_SWAPS = 0
SWAP_IN_PASS = True

while SWAP_IN_PASS:
    SWAP_IN_PASS = False
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            NUM_SWAPS += 1
            SWAP_IN_PASS = True

print('Array is sorted in {} swaps.'.format(NUM_SWAPS))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))

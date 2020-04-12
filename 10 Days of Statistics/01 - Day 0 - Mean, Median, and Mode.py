# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
NUMBER = list(map(int, input().split()))

# Mean
SUM = 0

for i in NUMBER:
    SUM = SUM + i
print(float(SUM / N))

# Median
NUMBER = sorted(NUMBER)

if N % 2 == 0:
    A = NUMBER[N//2]
    B = NUMBER[N//2 - 1]
    print((A+B)/2)
else:
    print(NUMBER[N//2])

# Mode
MAX_1 = 0
NUMBER = sorted(NUMBER)

for i in NUMBER:
    COUNTER = 0
    INDEX = NUMBER.index(i)

    for j in range(INDEX, len(NUMBER)):
        if i == NUMBER[j]:
            COUNTER = COUNTER + 1
        if COUNTER > MAX_1:
            MAX_1 = COUNTER
            if MAX_1 == 1:
                MODE = NUMBER[0]
            else:
                MODE = i

print(MODE)

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-arrays/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    n = int(input())

    b = list(map(int, input().split(" ")))

    for i in range(1, n+1):
        print(b[n-i], end=" ")

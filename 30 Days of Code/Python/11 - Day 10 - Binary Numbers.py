# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

    n = int(input())
    bi = bin(n).replace('0b','')
    arr = bi.split('0')
    newarr = [len(arr[i]) for i in range(len(arr))]
    print(max(newarr))

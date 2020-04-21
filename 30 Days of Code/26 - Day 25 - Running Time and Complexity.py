# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
# Difficulty: Medium
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

# Note: 1 is NOT a prime number, that is, a number divisable by another number less or equal to the square root of the first number, it is NOT prime

for _ in range(int(input())):
    num = int(input())
    if num == 1:
        print("Not prime")
    else:
        if(num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            for i in range(3, int(num**(1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")

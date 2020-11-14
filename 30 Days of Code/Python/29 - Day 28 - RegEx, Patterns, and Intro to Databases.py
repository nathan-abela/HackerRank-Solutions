# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-regex-patterns/problem
# Difficulty: Medium
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

if __name__ == '__main__':
    N = int(input())
    LIST_VALUES = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if emailID.endswith("@gmail.com"):
            LIST_VALUES.append(firstName)

    LIST_VALUES.sort()
    for val in LIST_VALUES:
        print(val)

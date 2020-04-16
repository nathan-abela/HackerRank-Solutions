# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

m = int(input())

a = set(map(int, input().split()))

n = int(input())

b = set(map(int, input().split()))

# Difference in each sets
c = a.difference(b)
d = b.difference(a)

# Union of difference
e = c.union(d)

# Converting set to a list
RESULT = list(e)

# Sorting
RESULT.sort()

# Iteration
for i in range(len(RESULT)):
    print(RESULT[i])

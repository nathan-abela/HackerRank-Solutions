# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
X = list(map(float, input().strip().split()))
Y = list(map(float, input().strip().split()))

X_COPY = X.copy()

Y_COPY = Y.copy()

X_COPY.sort()

XD = dict(zip(X_COPY, range(1, N+1)))

Y_COPY.sort()

YD = dict(zip(Y_COPY, range(1, N+1)))

RX = [XD[i] for i in X]

RY = [YD[i] for i in Y]

print(round(1-(6*sum([(RX-RY)**2 for RX, RY in zip(RX, RY)]))/((N**3)-N), 3))

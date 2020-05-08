# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/piling-up/problem
# Difficulty: Medium
# Max Score: 50
# Language: Python

# ========================
#         Solution
# ========================

ANS = []
T = int(input())

for _ in range(T):
    n = int(input())
    sl = list(map(int, input().split()))

    for _ in range(n-1):
        if sl[0] >= sl[len(sl)-1]:
            a = sl[0]
            sl.pop(0)
        elif sl[0] < sl[len(sl)-1]:
            a = sl[len(sl)-1]
            sl.pop(len(sl)-1)
        else:
            pass

        if len(sl) == 1:
            ANS.append("Yes")

        if((sl[0] > a) or (sl[len(sl)-1] > a)):
            ANS.append("No")
            break

print("\n".join(ANS))

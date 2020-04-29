# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/luck-balance/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the luckBalance function below.
def luckBalance(k, contests):
    con = contests
    con = sorted(con, reverse=True, key=lambda con: con[con[1] == 0])

    con_1 = [imp[0] for i, imp in enumerate(sorted(con)) if imp[1] == 0]

    con_2 = [imp[0] for j, imp in enumerate(sorted(con[0:k], reverse=True)) if imp[1] == 1]

    con_3 = [imp[0] for l, imp in enumerate(sorted(con[k:], reverse=True)) if imp[1] == 1]

    max_luck = sum(con_1)+sum(con_2)-sum(con_3)

    return max_luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    CONTESTS = []

    for _ in range(n):
        CONTESTS.append(list(map(int, input().rstrip().split())))

    RESULT = luckBalance(k, CONTESTS)

    fptr.write(str(RESULT) + '\n')
    fptr.close()

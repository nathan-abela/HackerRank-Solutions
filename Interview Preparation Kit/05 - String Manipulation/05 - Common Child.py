# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/common-child/problem
# Difficulty: Medium
# Max Score: 60
# Language: Python
# Compiler: Pypy3 - Due to timeout

# ========================
#         Solution
# ========================

import os

# Complete the commonChild function below.
def commonChild(s_1, s_2):
    last_row = [0]*(len(s_1)+1)

    for i in range(1, len(s_1)+1):
        current = [0]
        for j in range(1, len(s_2)+1):
            if s_1[i-1] == s_2[j-1]:
                current.append(last_row[j-1]+1)
            else:
                current.append(max(last_row[j], current[-1]))
        last_row = current

    return last_row[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    S_1 = input()
    S_2 = input()
    RESULT = commonChild(S_1, S_2)

    fptr.write(str(RESULT) + '\n')
    fptr.close()

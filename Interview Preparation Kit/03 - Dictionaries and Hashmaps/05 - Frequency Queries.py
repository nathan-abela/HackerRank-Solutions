# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/frequency-queries/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the freqQuery function below.
def freqQuery(queries):
    count = dict()
    result = list()

    for q in queries:
        if q[0] == 1:
            try:
                count[q[1]] += 1
            except:
                count[q[1]] = 1
        elif q[0] == 2:
            try:
                count[q[1]] -= 1
                if count[q[1]] == 0:
                    del count[q[1]]
            except:
                continue
        else:
            if q[1] in set(count.values()):
                result.append('1')
            else:
                result.append('0')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()

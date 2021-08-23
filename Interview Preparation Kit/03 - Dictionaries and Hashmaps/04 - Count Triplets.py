# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/count-triplets-1/problem
# Difficulty: Medium
# Max Score: 35
# Language: Python

# ========================
#         Solution
# ========================

import os

# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr) <= 2:
        return 0

    map_arr = {}
    map_doubles = {}
    count = 0

    # Traversing the array from rear, helps to avoid division
    for x in arr[::-1]:
        r_x = r*x
        r_r_x = r*r_x

        # Case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # Case: x is the second element (x/r, x, x*r)
        map_doubles[(x, r_x)] = map_doubles.get((x, r_x), 0) + map_arr.get(r_x, 0)

        # Case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')
    fptr.close()

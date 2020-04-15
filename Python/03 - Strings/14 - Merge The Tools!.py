# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Difficulty: Medium
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

def merge_the_tools(string, k):
    x = [string[i:i+k] for i in range(0, len(string), k)]

    for i in x:
        j = 0
        short = ""
        for _ in i:
            if i.index(_) == j:
                short += _
            j += 1
        print(short)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

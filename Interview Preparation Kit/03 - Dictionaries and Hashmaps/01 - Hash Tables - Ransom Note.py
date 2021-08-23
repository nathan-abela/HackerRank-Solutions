# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Difficulty: Easy
# Max Score: 25
# Language: Python

# ========================
#         Solution
# ========================

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine.sort()
    note.sort()

    for word in note:
        if word not in magazine:
            flag = False
            break
        else:
            magazine.remove(word)
        flag = True

    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    MAGAZINE = input().rstrip().split()
    NOTE = input().rstrip().split()
    checkMagazine(MAGAZINE, NOTE)

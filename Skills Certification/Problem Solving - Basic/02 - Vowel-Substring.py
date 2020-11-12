# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/skills-verification/problem_solving_basic
# Difficulty: Basic
# Language: Python 3

# ========================
#         Question
# ========================

# Given a string of lowercase English letters and an integer of the substring length, determine the substring of that length that contains the most vowels.
# Vowels are in the set {a, e, i, o, u}. If there is more than one substring with the maximum number of vowels, return the one that starts at the lowest index.
# If there are no vowels in the input string, return the string 'Not found!' without quotes.

# Example 1

# s = 'caberqiitefg'
# k = 5
# The substring of length k = 5 that contains the maximum number of vowels is 'erqii' with 3 vowels.
# The final answer is 'erqii'.

# Example 2

# s = 'aeiouia'
# k = 3

# All of the characters are vowels, so any substring of length 3 will have 3 vowels. The lowest index substring is at index 0, 'aei'.

# Function Description

# findSubstring has the following parameters:
# s: a string
# k: an integer

# Returns:

# string: a string containing the final answer

# ========================
#         Solution
# ========================

import os

def findSubstring(s, k):
    n = len(s)
    vow = 0

    for i in range(k):
        if s[i] in 'aeiou':
            vow += 1
    max_vow = vow
    temp_str = s[:k]
    temp = vow

    for i in range(1, n - k + 1):
        if s[i - 1] in 'aeiou':
            temp -= 1
        if s[i + k - 1] in 'aeiou':
            temp += 1
        if max_vow < temp:
            max_vow = temp
            temp_str = s[i:i + k]
    if max_vow == 0:
        return 'Not found!'

    return temp_str

# Below is given
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()

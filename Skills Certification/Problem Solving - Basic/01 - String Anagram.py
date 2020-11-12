# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/skills-verification/problem_solving_basic
# Difficulty: Basic
# Language: Python 3

# ========================
#         Question
# ========================

# An anagram of a string is another string with the same characters in the same frequency, in any order.
# For example 'abc', 'bca', 'acb', 'bac', 'cba', 'cab' are all anagrams of the string 'abc'. 
# Given two arrays of strings, for every string in one list, determine how many anagrams of it are in the other list.
# Write a function that receives dictionary and query, two string arrays.
# It should return an array of integers where each element i contains the number of anagrams of query[i] that exist in dictionary.

# Example

# dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
# query = ["a", "nark", "bs", "hack", "stair"]

# - query[0] = 'a' has 2 anagrams in dictionary: 'a' and 'a'.
# - query[1] = 'nark' has 2 anagrams in dictionary: 'rank' and 'kran'.
# - query[2] = 'bs' has 0 anagrams in dictionary.
# - query[3] = 'hack' has 3 anagrams in dictionary: 'hack', 'khac' and 'ackh'.
# - query[4] = 'stair'has 1 anagram in dictionary:'raits'. While the characters are the same in 'stairs', the frequency of 's' differs, so it is not an anagram.
# The final answer is [2, 2, 0, 3, 1].

# Function Description

# stringAnagram has the following parameters:
# string dictionary[n]: an array of strings to search in
# string query[q]:an array of strings to search for

# Returns

# int[q]:an array of integers where the i<sup>th</sup>value is the answer to query[i]

# ========================
#         Solution
# ========================

import os
from collections import Counter

def stringAnagram(dictionary, query):
    dict = ["".join(sorted(word)) for word in dictionary]
    q = ["".join(sorted(word)) for word in query]

    result = []
    count = Counter(dict)

    for word in q:
        if word in count.keys():
            result.append(count[word])
        else:
            result.append(0)

    return result

# Below is given
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

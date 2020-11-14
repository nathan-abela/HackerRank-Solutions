# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-queues-stacks/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import sys # Solution made without using the required library

class Solution:
    # Write your code here
    def __init__(self):
        self.top = 0
        self.rear = 0
        self.a = list()
        self.r = list()

    def pushCharacter(self, char):
        self.a.append(char)
        self.top += 1

    def enqueueCharacter(self, char):
        self.r.append(char)
        self.rear += 1

    def popCharacter(self):
        self.top -= 1
        return self.a[self.top]

    def dequeueCharacter(self):
        return self.r[i]

# Read the string s
s = input()

# Create the Solution class object
obj = Solution()

l = len(s)

# Push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

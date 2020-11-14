# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        #Write your code here
        if head is None:
            return head
        values = [head.data]
        temp = head.next
        prev = head
        while temp:
            if temp.data in values:
                temp = temp.next
            else:
                values.append(temp.data)
                prev.next = temp
                prev = prev.next
                temp = temp.next
        prev.next = None
        return head

mylist= Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)

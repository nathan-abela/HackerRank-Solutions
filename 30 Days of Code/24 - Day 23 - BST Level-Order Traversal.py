# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-binary-trees/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import sys

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        nodes_queue = []
        data_list = []
        temp_node = root

        while temp_node:
            data_list.append(temp_node.data)
            if temp_node.left is not None:
                nodes_queue.append(temp_node.left)
            if temp_node.right is not None:
                nodes_queue.append(temp_node.right)
            if len(nodes_queue) == 0:
                break
            temp_node = nodes_queue.pop(0)

        print(' '.join(list(map(str, data_list))))

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/skills-verification/python_basic
# Difficulty: Basic
# Language: Python 3

# ========================
#         Question
# ========================

# A multiset is the same as a set except that an element might occur more than once in a multiset. Implement a multiset data structure in Python. Given a template for the Multiset class, implement 4 methods:
	
# - add(self, val): adds val to the multiset
# - remove(self, val): if val is in the multiset, removes val from the multiset; otherwise, do nothing
# - contains__(self, val): returns True if val is in the multiset; otherwise, it returns False
# - len__(self): returns the number of elements in the multiset
	
# Additional methods are allowed as necessary

# The implementations of the 4 required methods will be tested by a provided code stub on several input files. Each input file contains several operations, each of one of the below types. Values returned by query and size operations are appended to a result list, which is printed as the output by the provided code stub.

# - add val: calls add(val) on the Multiset instance
# - remove val: calls remove(val) on the Multiset instance
# - query val: appends the result of expression val in m, where m is an instance of Multiset, and appends the value of that expression to the result list
# - size: calls len(m), where m is an instance of Multiset, and appends the returned value to the result list

# ========================
#         Solution
# ========================

import os

class Multiset:
    def __init__(self):
        self.collection = list()

    def add(self, val):
        # Adds one occurrence of val from the multiset, if any
        self.collection.append(val)

    def remove(self, val):
        # Removes one occurrence of val from the multiset, if any
        if val in self.collection:
            self.collection.remove(val)
        else:
            return False

    def __contains__(self, val):
        # Returns True when val is in the multiset, else returns False
        if val in self.collection:
            return True
        else:
            return False

    def __len__(self):
        # Returns the number of elements in the multiset
        return len(self.collection)

# Below is given
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

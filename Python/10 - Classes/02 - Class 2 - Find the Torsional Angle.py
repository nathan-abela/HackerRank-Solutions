# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
# Difficulty: Easy
# Max Score: 20
# Language: Python

# ========================
#         Solution
# ========================

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return  Points((self.x-no.x), (self.y-no.y), (self.z-no.z))

    def dot(self, no):
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)

    def cross(self, no):
        return Points((self.y*no.z-self.z*no.y), (self.z*no.x-self.x*no.z), (self.x*no.y-self.y*no.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    POINTS = list()
    for i in range(4):
        A = list(map(float, input().split()))
        POINTS.append(A)

    A, B, C, D = Points(*POINTS[0]), Points(*POINTS[1]), Points(*POINTS[2]), Points(*POINTS[3])
    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)
    ANGLE = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))

    print("%.2f" % math.degrees(ANGLE))

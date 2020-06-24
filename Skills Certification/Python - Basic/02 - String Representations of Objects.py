# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/skills-verification/python_basic
# Difficulty: Basic
# Language: Python 3

# ========================
#         Question
# ========================

# Implement two vehicle classes

# Car:

# - The constructor for Car must take two arguments. The first of them is its maximum speed, and the second one is a string that denotes the units in which the speed is given: either "km/h" or "mph".
	
# - The class must be implemented to return a string based on the arguments. For example, if car is an object of class Car with a maximum speed of 120, and the unit is "km/h", then printing car prints the following string: "Car with the maximum speed of 120 km/h", without quotes. If the maximum speed is 94 and the unit is "mph", then printing car prints in the following string: "Car with the maximum speed of 94 mph", without quotes.

# Boat:

# The constructor for Boat must take a single argument denoting its maximum speed in knots.

# - The class must be implemented to return a string based on the argument. For example, if boat is an object of class Boat with a maximum speed of 82, then printing boat prints the following string: "Boat with the maximum speed of 82 knots", without quotes.

# ========================
#         Solution
# ========================

import os

class Car:
    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit

    def __str__(self):
        result = "Car with the maximum speed of {} {}"

        return result.format(self.speed, self.unit)

class Boat:
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        result = "Boat with the maximum speed of {} knots"

        return result.format(self.speed)

# Below is given
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()

# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/30-inheritance/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
    def print_person(self):
        '''Print Student Name and ID'''
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)

class Student(Person):
    '''Class Constructor'''
    # Parameters:
    # first_name - A string denoting the Person's first name.
    # last_name - A string denoting the Person's last name.
    # id - An integer denoting the Person's ID number.
    # scores - An array of integers denoting the Person's test scores.

    # Write your constructor here
    def __init__(self, first_name, last_name, id_number, scores):
        self.scores = scores
        super().__init__(first_name, last_name, id_number)

    # Function Name: calculate
    # Return: A character denoting the grade.

    # Write your function here
    def calculate(self):
        '''Calcuate Scores'''

        average = sum(self.scores) / len(self.scores)
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average <= 90:
            return 'E'
        elif 70 <= average <= 80:
            return 'A'
        elif 55 <= average <= 70:
            return 'P'
        elif 40 <= average <= 55:
            return 'D'
        else:
            return 'T'

LINE = input().split()
FIRST_NAME = LINE[0]
LAST_NAME = LINE[1]
ID_NUMBER = LINE[2]

NUM_SCORES = int(input()) # not needed for Python
SCORES = list( map(int, input().split()))

S = Student(FIRST_NAME, LAST_NAME, ID_NUMBER, SCORES)
S.print_person()

print("Grade:", S.calculate())

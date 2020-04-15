# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/text-alignment/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

# Replace all ______ with rjust, ljust or center

THICKNESS = int(input()) #This must be an odd number
c = 'H'

# Top Cone
for i in range(THICKNESS):
    print((c*i).rjust(THICKNESS-1)+c+(c*i).ljust(THICKNESS-1))

# Top Pillars
for i in range(THICKNESS+1):
    print((c*THICKNESS).center(THICKNESS*2)+(c*THICKNESS).center(THICKNESS*6))

# Middle Belt
for i in range((THICKNESS+1)//2):
    print((c*THICKNESS*5).center(THICKNESS*6))    

# Bottom Pillars
for i in range(THICKNESS+1):
    print((c*THICKNESS).center(THICKNESS*2)+(c*THICKNESS).center(THICKNESS*6))    

# Bottom Cone
for i in range(THICKNESS):
    print(((c*(THICKNESS-i-1)).rjust(THICKNESS)+c+(c*(THICKNESS-i-1)).ljust(THICKNESS)).rjust(THICKNESS*6))

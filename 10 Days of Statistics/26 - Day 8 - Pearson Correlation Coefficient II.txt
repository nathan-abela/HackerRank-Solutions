========================
      Information
========================

Direct Link: https://www.hackerrank.com/challenges/s10-mcq-7/problem
Difficulty: Easy
Max Score: 30
Language: Python
Multiple Choice Question - No code required

========================
        Solution
========================

Rewriting both lines in the form of y = mx + c
y = (-3/4)*x - 2
x = (-3/4)*y + (-7/4)

c1 = -3/4
c2 = -3/4

Let x_std be the standard deviation of x, and let y_std be the standard deviation of y

p = c1(x_std / y_std)
p = c2(y_std / x_std)

Multiplying both questions:
p^2 = c1 * c2
p^2 = (-3/4) * (-3/4)
p^2 = 9/16
p = +/-(3/4)

Since x_std and y_std have to be positive. So p shares the same sign as c1 or c2. Thus, -3/4

>>> -3/4
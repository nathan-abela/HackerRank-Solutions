-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/the-blunder/problem
-- Difficulty: Easy
-- Max Score: 15
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT CEILING((SUM(Salary) - SUM(REPLACE(Salary, '0', ""))) / COUNT(*))
FROM EMPLOYEES;

-- ========================
--       Explanation
-- ========================

-- CEILING() used to return the smallest integer value that is larger than or equal to a number

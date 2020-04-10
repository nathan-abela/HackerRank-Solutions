-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/salary-of-employees/problem
-- Difficulty: Easy
-- Max Score: 10
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT name
FROM Employee
WHERE salary > 2000 AND months < 10
ORDER BY employee_id;

-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/earnings-of-employees/problem
-- Difficulty: Easy
-- Max Score: 20
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT salary * months, COUNT(*)
FROM Employee
GROUP BY 1
ORDER BY 1 DESC 
LIMIT 1;

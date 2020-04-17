-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/the-pads/problem
-- Difficulty: Medium
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT CONCAT(NAME, "(", LEFT(Occupation , 1), ")")
FROM OCCUPATIONS
ORDER BY NAME ASC;

SELECT CONCAT("There are a total of ", COUNT(Occupation), ' ', LOWER(Occupation), "s.")
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation ASC;

-- ========================
--       Explanation
-- ========================

-- CONCAT() function adds two or more expressions together

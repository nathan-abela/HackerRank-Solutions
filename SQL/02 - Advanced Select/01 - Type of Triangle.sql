-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Difficulty: Easy
-- Max Score: 20
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT
CASE
    WHEN A + B <= C OR A + C <= B OR B + C <= A
        THEN 'Not A Triangle'
    WHEN A = B AND A = C AND B = C
        THEN 'Equilateral'
    WHEN A = B OR A = C OR B = C
        THEN 'Isosceles'
    ELSE 'Scalene'
END
FROM TRIANGLES;

-- ========================
--       Explanation
-- ========================

-- 'CASE' goes through conditions and return a value when the first condition is met (like an IF-ELSE statement). So, once a condition is true, it will stop reading and return the result.
-- If no conditions are true, it will return the value in the ELSE clause.
-- If there is no ELSE part and no conditions are true, it returns NULL.

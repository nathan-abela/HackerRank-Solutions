-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/binary-search-tree-1/problem
-- Difficulty: Medium
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT
CASE
    WHEN P IS NULL
        THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT DISTINCT P FROM BST)
        THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf')
END
FROM BST
ORDER BY N ASC;

-- ========================
--       Explanation
-- ========================

-- 'CASE' goes through conditions and return a value when the first condition is met (like an IF-ELSE statement). So, once a condition is true, it will stop reading and return the result.
-- If no conditions are true, it will return the value in the ELSE clause.
-- If there is no ELSE part and no conditions are true, it returns NULL.

-- CONCAT() function adds two or more expressions together

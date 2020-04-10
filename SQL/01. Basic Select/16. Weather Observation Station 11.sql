-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- Difficulty: Easy
-- Max Score: 15
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT DISTINCT(CITY)
FROM STATION
WHERE RIGHT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U') OR LEFT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication

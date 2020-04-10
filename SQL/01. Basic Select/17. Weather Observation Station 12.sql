-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-12/problem
-- Difficulty: Easy
-- Max Score: 15
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT DISTINCT(CITY)
FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U') AND RIGHT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication

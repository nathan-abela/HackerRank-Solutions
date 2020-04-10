-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
-- Difficulty: Easy
-- Max Score: 10
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT DISTINCT(CITY)
FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication

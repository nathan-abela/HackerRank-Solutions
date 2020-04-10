-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-4/problem
-- Difficulty: Easy
-- Max Score: 10
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication
-- COUNT() used to return the number of rows in a table

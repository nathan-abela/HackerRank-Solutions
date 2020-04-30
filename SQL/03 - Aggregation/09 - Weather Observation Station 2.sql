-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-2/problem
-- Difficulty: Easy
-- Max Score: 15
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT ROUND(SUM(LAT_N), 2),
       ROUND(SUM(LONG_W), 2)
FROM STATION;

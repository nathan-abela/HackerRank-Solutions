-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-19/problem
-- Difficulty: Medium
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT ROUND(SQRT(POW(MAX(LAT_N)  - MIN(LAT_N),  2) +
                  POW(MAX(LONG_W) - MIN(LONG_W), 2)), 4)
FROM STATION;

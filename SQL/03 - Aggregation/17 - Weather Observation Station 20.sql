-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-20/problem
-- Difficulty: Medium
-- Max Score: 40
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT ROUND(S.LAT_N, 4)
FROM STATION S
WHERE (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N < S.LAT_N)
    = (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N > S.LAT_N);

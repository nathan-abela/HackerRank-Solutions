-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-3/problem
-- Difficulty: Easy
-- Max Score: 10
-- DBMS: mySQL
-- Weather Observation Station 2 is not missing, it will be carried out in Aggregation

-- ========================
--         Solution
-- ========================

SELECT DISTINCT(CITY)
FROM STATION
WHERE MOD(ID, 2) = 0;

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication
-- MOD() used to get the remainder from a division

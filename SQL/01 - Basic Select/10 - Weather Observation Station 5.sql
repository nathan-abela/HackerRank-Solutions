-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/weather-observation-station-5/problem
-- Difficulty: Easy
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY ASC
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC
LIMIT 1;


//for the ms sql server 

SELECT Top 1 CITY, LEN(CITY)
FROM STATION
ORDER BY LEN(CITY), CITY ASC
;

SELECT Top 1 CITY, LEN(CITY)
FROM STATION
ORDER BY LEN(CITY) DESC
 ;
-- ========================
--       Explanation
-- ========================

-- LENGTH() used to return the number of characters in a string
-- LIMIT 1 used so that each query only returns the first result, thus, returning the longest and shortest city names.

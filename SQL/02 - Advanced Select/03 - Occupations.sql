-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/occupations/problem
-- Difficulty: Medium
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SET @d=0, @a=0, @p=0, @s=0;
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM
       (SELECT
              CASE Occupation
                     WHEN 'Doctor'
                            THEN @d:=@d+1
                     WHEN 'Professor'
                            THEN @a:=@a+1
                     WHEN 'Singer'
                            THEN @p:=@p+1
                     WHEN 'Actor'
                            THEN @s:=@s+1
              END AS RowLine,
              CASE
                     WHEN Occupation = 'Doctor'
                            THEN Name
              END AS Doctor,
              CASE
                     WHEN Occupation = 'Professor'
                            THEN Name
              END AS Professor,
              CASE
                     WHEN Occupation = 'Singer'
                            THEN Name
              END AS Singer,
              CASE
                     WHEN Occupation = 'Actor'
                            THEN Name
              END AS Actor
              FROM OCCUPATIONS
       ORDER BY Name) AS t
GROUP BY RowLine;

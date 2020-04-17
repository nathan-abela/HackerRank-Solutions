-- ========================
--       Information
-- ========================

-- Direct Link: https://www.hackerrank.com/challenges/the-company/problem
-- Difficulty: Medium
-- Max Score: 30
-- DBMS: mySQL

-- ========================
--         Solution
-- ========================

SELECT c.company_code, c.founder, 
      COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code),
      COUNT(DISTINCT m.manager_code), COUNT(DISTINCT e.employee_code)
FROM Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e
WHERE c.company_code = l.company_code AND 
      l.lead_manager_code = s.lead_manager_code AND
      s.senior_manager_code = m.senior_manager_code AND
      m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder ORDER BY c.company_code;

-- ========================
--       Explanation
-- ========================

-- DISTINCT() used to avoid duplication
-- COUNT() used to return the number of rows in a table

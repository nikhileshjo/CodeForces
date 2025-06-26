--Nth Highest Salary
--https://leetcode.com/problems/nth-highest-salary/description/

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT(
        SELECT DISTINCT sal AS getNthHighestSalary
        FROM (
            SELECT DENSE_RANK() OVER(ORDER BY e.salary) sal_rank, e.salary AS sal
            FROM employee e
        )
        WHERE sal_rank = N
    )
  );
END;
$$ LANGUAGE plpgsql;
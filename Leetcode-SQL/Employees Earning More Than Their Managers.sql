--https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/1677022180/

SELECT
    e.name AS Employee
FROM
    employee e
    INNER JOIN
    employee m
    ON (e.managerID = m.id)
WHERE e.salary > m.salary;
--Customers Who Never Order
-- https://leetcode.com/problems/customers-who-never-order/description/

SELECT
    name AS customers
FROM
    customers c
    LEFT OUTER JOIN
    orders o
    ON (c.id = o.customerid)
WHERE o.id IS NULL;
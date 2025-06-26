--https://leetcode.com/problems/duplicate-emails/description/
SELECT 
    email
FROM 
    person
GROUP BY
    email
HAVING 
    COUNT(*) > 1;
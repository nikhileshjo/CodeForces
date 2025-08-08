--Link: https://www.hackerrank.com/challenges/sql-projects/

WITH start_dates AS (
    SELECT
        start_date
    FROM
        projects
    WHERE
        start_date NOT IN (SELECT end_date FROM projects)
),
end_dates AS (
    SELECT
        end_date
    FROM
        projects
    WHERE
        end_date NOT IN (SELECT start_date FROM projects)
)
SELECT
    s.start_date AS start_date,
    MIN(e.end_date) AS end_date
FROM
    start_dates s
    CROSS JOIN
    end_dates e
WHERE
    e.end_date > s.start_date
GROUP BY
    s.start_date
ORDER BY
    MIN(e.end_date)-s.start_date, s.start_date; 
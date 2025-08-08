--Link: https://www.hackerrank.com/challenges/contest-leaderboard

SELECT
    h.hacker_id AS hacker_id,
    h.name AS name,
    SUM(ms.score) AS total_score
FROM
    (
	SELECT
        hacker_id,
        challenge_id,
        MAX(score) AS score
    FROM
        submissions
    GROUP BY
        hacker_id,
        challenge_id
	) ms
    INNER JOIN
    hackers h
    ON (ms.hacker_id = h.hacker_id)
GROUP BY
    h.hacker_id,
    h.name
HAVING
    SUM(ms.score) > 0
ORDER BY
    total_score DESC, hacker_id ASC;
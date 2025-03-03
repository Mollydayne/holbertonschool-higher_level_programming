--  script that lists the number of records with the same score - task 15. Number by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY NUMBER DESC;

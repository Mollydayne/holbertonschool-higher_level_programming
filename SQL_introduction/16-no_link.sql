-- script that lists all records of the table second_table - task 16. Say my name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

-- lists all records of second table where name is not NULL
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

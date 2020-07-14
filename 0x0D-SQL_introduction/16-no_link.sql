-- Lists all records in `second_table` in descending order
-- Do not show scores that has'nt name values.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

-- Lists the number of records with the same score in `second_table`.
SELECT score, COUNT(*) FROM second_table GROUP BY score ORDER BY socre DESC;

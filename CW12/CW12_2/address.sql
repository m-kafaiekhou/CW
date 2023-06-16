----part1
--SELECT DISTINCT district FROM address ORDER BY district LIMIT 5;

----part2
--SELECT COUNT(*) FROM (SELECT DISTINCT district FROM address) AS unq; 


-----part3
---- counts how many time a district has been repeated does two queries
-- (SELECT DISTINCT district, COUNT(district) AS cnt FROM address GROUP BY district ORDER BY cnt LIMIT 3)
-- UNION ALL
-- (SELECT DISTINCT district, COUNT(district) AS cnt FROM address GROUP BY district ORDER BY cnt DESC LIMIT 3);

---- counts how many time a district has been repeated does one query(more efficient??)
-- WITH scanner AS (
--     SELECT DISTINCT district, COUNT(*) AS cnt, 
--            ROW_NUMBER() OVER (ORDER BY COUNT(*) ASC) AS first_rows, 
--            ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS last_rows
--     FROM address
--     GROUP BY district
-- )

-- SELECT district, cnt 
-- FROM scanner 
-- WHERE scanner.first_rows IN (1, 2, 3) OR scanner.last_rows IN (1, 2, 3) ORDER BY cnt;

---- counts how many addresses(address or address2) are in one district(one query, top3 and bottom 3)
WITH scanner AS (
    SELECT DISTINCT district, 
           COALESCE(COUNT(NULLIF(address, ''))) + COALESCE(COUNT(NULLIF(address2, ''))) AS cnt,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) ASC) AS first_rows, 
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS last_rows
    FROM address
    GROUP BY district
)

SELECT district, cnt 
FROM scanner 
WHERE scanner.first_rows IN (1, 2, 3) OR scanner.last_rows IN (1, 2, 3) 
ORDER BY cnt;

---part4
-- SELECT address, address2, district FROM address WHERE district IN ('California', 'Alberta');
--SELECT DISTINCT district FROM address ORDER BY district LIMIT 5;

--SELECT COUNT(*) FROM (SELECT DISTINCT district FROM address) AS unq; 


-- (SELECT DISTINCT district, COUNT(district) AS cnt FROM address GROUP BY district ORDER BY cnt LIMIT 3)
-- UNION ALL
-- (SELECT DISTINCT district, COUNT(district) AS cnt FROM address GROUP BY district ORDER BY cnt DESC LIMIT 3);

-- WITH scanner AS (
--     SELECT DISTINCT district, COUNT(district), ROW_NUMBER() OVER (
--         ORDER  BY COUNT(district) ASC) AS first_rows, ROW_NUMBER() OVER
--          (ORDER  BY COUNT(district) DESC) AS last_rows
-- FROM address)

-- SELECT district, cnt FROM scanner 
-- WHERE scanner.first_rows IN (1 OR 2 OR 3) OR 
-- scanner.last_rows IN (1 OR 2 OR 3);

WITH scanner AS (
    SELECT DISTINCT district, COUNT(*) AS cnt, 
           ROW_NUMBER() OVER (ORDER BY COUNT(*) ASC) AS first_rows, 
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS last_rows
    FROM address
    GROUP BY district
)

SELECT district, cnt 
FROM scanner 
WHERE scanner.first_rows IN (1, 2, 3) OR scanner.last_rows IN (1, 2, 3) ORDER BY cnt;
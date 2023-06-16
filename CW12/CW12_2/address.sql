--SELECT DISTINCT district FROM address ORDER BY district LIMIT 5;

SELECT COUNT(*) FROM (SELECT DISTINCT district FROM address) AS unq;

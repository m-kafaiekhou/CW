SELECT * FROM film WHERE rental_duration > 4;  -- 1

SELECT * FROM film WHERE rental_duration > 2 AND rental_duration < 5;  -- 2

SELECT * FROM film WHERE rental_duration > 2 AND rental_duration < 5 ORDER BY last_update ASC; --3

SELECT * FROM film WHERE rental_duration > 2 AND rental_duration < 5 ORDER BY last_update DESC; --3

SELECT * FROM film WHERE rental_duration > 4 ORDER BY title ASC; -- 3

SELECT * FROM film WHERE rental_duration > 4 ORDER BY title DESC; -- 3

SELECT ROUND(AVG(length)), MAX(length), MIN(length) FROM film; -- 4
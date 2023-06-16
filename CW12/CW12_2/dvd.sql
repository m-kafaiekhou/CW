-- SELECT * FROM film WHERE rental_duration > 4;

-- SELECT * FROM film WHERE rental_duration > 2 AND rental_duration < 5;

-- SELECT * FROM film WHERE rental_duration > 2 AND rental_duration < 5 ORDER BY last_update ASC;

-- SELECT * FROM film WHERE rental_duration > 2 AND rental_duration < 5 ORDER BY last_update DESC;

-- SELECT * FROM film WHERE rental_duration > 4 ORDER BY title ASC;

-- SELECT * FROM film WHERE rental_duration > 4 ORDER BY title DESC;

SELECT ROUND(AVG(length)), MAX(length), MIN(length) FROM film;
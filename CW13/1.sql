-- SELECT film.title, category.name as category
-- FROM film
-- join film_category on film_category.film_id = film.film_id
-- join category on category.category_id = film_category.category_id;


-- SELECT film.title, category.name as category, film.release_year 
-- FROM film
-- join film_category on film_category.film_id = film.film_id
-- join category on category.category_id = film_category.category_id
-- WHERE category.name IN ('Action', 'Comedy', 'Family'); 


SELECT category.name, COUNT(*) as count
FROM film
join film_category on film_category.film_id = film.film_id
join category on category.category_id = film_category.category_id
GROUP BY category.name
ORDER BY count DESC;
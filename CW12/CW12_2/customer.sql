---part1
-- SELECT first_name, last_name FROM customer WHERE first_name ILIKE 'JEN%';

-- ---part2
-- SELECT first_name, last_name FROM customer WHERE first_name ILIKE '%ER%';

-- ---part3
-- SELECT first_name, last_name FROM customer WHERE first_name ILIKE '%l';

---part4
SELECT first_name, last_name FROM customer WHERE first_name NOT ILIKE 'JEN%'
USE sakila;
SELECT * FROM film;
SELECT title, rating, release_year FROM film;

SELECT first_name, last_name FROM sakila.actor
ORDER BY first_name ASC, last_name DESC;
SELECT COUNT(DISTINCT first_name) FROM sakila.actor;

SELECT * FROM sakila.language LIMIT 5 OFFSET 1;


SELECT title, release_year, length, rating, replacement_cost FROM sakila.film
ORDER BY length DESC, replacement_cost ASC
LIMIT 20;
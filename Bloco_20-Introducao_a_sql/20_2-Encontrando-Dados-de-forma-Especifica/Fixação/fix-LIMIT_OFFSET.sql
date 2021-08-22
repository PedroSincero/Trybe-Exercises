-- 1. Tranquilo, não é? Agora, olhando a resultado a seguir, qual query eu teria que montar para trazer os 10 primeiros resultados, a partir da JOHNNY?
SELECT * FROM sakila.actor LIMIT 10 OFFSET 5;

-- Escreva uma query que exiba todos os filmes cadastrados no banco de dados.

USE sakila;
-- Escreva uma query que exiba apenas o nome dos filmes, seu ano de lançamento e sua classificação .

SELECT * FROM film;
-- Quantos filmes temos cadastrados?
SELECT title, rating, release_year FROM film;
-- Ordene os valores na tabela em ordem crescente de sobrenomes e em ordem decrescente de nome.
SELECT first_name, last_name FROM sakila.actor
ORDER BY first_name ASC, last_name DESC;
-- Quantos sobrenomes únicos temos na tabela?
SELECT COUNT(DISTINCT first_name) FROM sakila.actor;
-- Vá até à tabela language do sakila e crie uma pesquisa que mostre os 5 idiomas cadastrados , mas não mostre o idioma "english"
SELECT * FROM sakila.language LIMIT 5 OFFSET 1;

-- Agora vamos tentar fazer o seguinte: Crie uma query para encontrar os 20 primeiros filmes , incluindo o título , o ano de lançamento , a duração e a classificação indicativa e o custo de substituição . Ordene os resultados pelos filmes com a maior duração e depois pelo menor custo de substituição.
SELECT title, release_year, length, rating, replacement_cost FROM sakila.film
ORDER BY length DESC, replacement_cost ASC
LIMIT 20;
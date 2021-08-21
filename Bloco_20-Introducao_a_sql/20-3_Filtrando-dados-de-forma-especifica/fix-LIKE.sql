-- Utilizações LIKE
-- Encontra qualquer resultado finalizando com "don"
SELECT * FROM sakila.film
WHERE title LIKE '%don';

-- Encontra qualquer resultado iniciando com "plu"
SELECT * FROM sakila.film
WHERE title LIKE 'plu%';

-- Encontra qualquer resultado que contém "plu"
SELECT * FROM sakila.film
WHERE title LIKE '%plu%';

-- Encontra qualquer resultado que inicia com "p" e finaliza com "r"
SELECT * FROM sakila.film
WHERE title LIKE 'p%r';

-- Encontra qualquer resultado em que o segundo caractere da frase é "C"
SELECT * FROM sakila.film
WHERE title LIKE '_C%';

-- Encontra qualquer resultado em que o título possui exatamente 8 caracteres
SELECT * FROM sakila.film
WHERE title LIKE '________';

-- Encontra todas as palavras com no mínimo 3 caracteres e que iniciam com E
SELECT * FROM sakila.film
WHERE title LIKE 'E__%';


-- FIX
-- 1. Mostre todos os detalhes dos filmes que contêm a palavra ace no nome. 
USE sakila;
SELECT * FROM film
WHERE title LIKE '%ace%';
-- 2. Mostre todos os detalhes dos filmes cujas descrições finalizam com china . 
USE sakila;
SELECT * FROM film
WHERE description LIKE '%china';
-- 3. Mostre todos os detalhes dos dois filmes cujas descrições contêm a palavra girl e o título finaliza com a palavra lord . 
USE sakila;
SELECT * FROM film
WHERE description LIKE '%girl%' AND title LIKE '%lord';
-- 4. Mostre os dois casos em que, a partir do 4° caractere no título do filme, tem-se a palavra gon . 
USE sakila;
SELECT * FROM film
WHERE title LIKE '___gon%';
-- 5. Mostre o único caso em que, a partir do 4° caractere no título do filme, tem-se a palavra gon e a descrição contém a palavra Documentary . 
USE sakila;
SELECT * FROM film
WHERE title LIKE '___gon%' AND description LIKE '%Documentary%';
-- 6. Mostre os dois filmes cujos títulos ou finalizam com academy ou iniciam com mosquito . 
USE sakila;
SELECT * FROM film
WHERE title LIKE '%academy' OR title LIKE 'mosquito%';
-- 7. Mostre os seis filmes que contêm as palavras monkey e sumo em suas descrições. 
USE sakila;
SELECT * FROM film
WHERE description LIKE '%monkey%' AND description LIKE '%sumo%';
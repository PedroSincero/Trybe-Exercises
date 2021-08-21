-- 1. Monte uma query que exiba seu nome na tela;
SELECT 'jhonatan';
-- 2. Monte uma query que exiba seu nome, sobrenome, cidade natal e idade na tela;
SELECT 'amanda', 'santos', 'Belo Horizonte', 19;
-- 3. Monte uma query que, além de exibir todas as informações já mencionadas, identifique cada coluna usando o AS , que é chamado de alias na linguagem SQL ( alias é como um apelido no português);
SELECT 'amanda' AS Nome, 'santos' AS Sobrenome, 'Belo Horizonte' AS 'Cidade Natal', 19 AS Idade;
-- 4. Qual é o resultado de 13 * 8 ? Descubra usando apenas o SELECT ;
SELECT 13*8;
-- 5. Monte uma query que exiba a data e hora atuais. Dê a essa coluna o nome "Data Atual".
SELECT now() as 'Data Atual';

-- 6. Escreva uma query que selecione todas as colunas da tabela city ;
SELECT * FROM sakila.city;
-- 7. Escreva uma query que exiba apenas as colunas first_name e last_name da tabela customer ;
SELECT first_name, last_name FROM sakila.customer;
-- 8. Escreva uma query que exiba todas as colunas da tabela rental ;
SELECT * FROM sakila.rental;
-- 9. Escreva uma query que exiba o título, a descrição e a data de lançamento dos filmes registrados na tabela film ;
SELECT title, description, release_year FROM sakila.film;
-- 10. Utilize o SELECT para explorar todas as tabelas do banco de dados.
SELECT * FROM sakila.nome_da_tabela;
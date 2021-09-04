// models/Author.js

const connection = require('./connection');

// Cria uma string com o nome completo do autor

const getNewAuthor = (authorData) => {
    const {
        id,
        firstName,
        middleName,
        lastName
    } = authorData;

    const fullName = [firstName, middleName, lastName]
        .filter((name) => name)
        .join(' ');

    return {
        id,
        firstName,
        middleName,
        lastName,
        name: fullName,
    };
};

// Converte o nome dos campos de snake_case para camelCase

const serialize = (authorData) => ({
    id: authorData.id,
    firstName: authorData.first_name,
    middleName: authorData.middle_name,
    lastName: authorData.last_name
});

// Busca todos os autores do banco.

const getAll = async () => {
    const [authors] = await connection.execute(
        'SELECT id, first_name, middle_name, last_name FROM model_example.authors;',
    );
    return authors.map(serialize).map(getNewAuthor);
};
/*
Busca um autor específico, a partir do seu ID
@param {String} id ID do autor a ser recuperado
*/

const findById = async (id) => {
    // Repare que substituímos o id por `?` na query.
    // Depois, ao executá-la, informamos um array com o id para o método `execute`.
    // O `mysql2` vai realizar, de forma segura, a substituição do `?` pelo id informado.
    const query = 'SELECT id, first_name, middle_name, last_name FROM model_example.authors WHERE id = ?'
    const [authorData] = await connection.execute(query, [id]);

    if (authorData.length === 0) return null;

    // Utilizamos [0] para buscar a primeira linha, que deve ser a única no array de resultados, pois estamos buscando por ID.
    const {
        firstName,
        middleName,
        lastName
    } = serialize(authorData[0]);

    return getNewAuthor({
        id,
        firstName,
        middleName,
        lastName
    });
};

const isValid = (firstName, middleName, lastName) => {
    if (!firstName || typeof firstName !== 'string') return false;
    if (!lastName || typeof lastName !== 'string') return false;
    if (middleName && typeof middleName !== 'string') return false;

    return true;
};

const create = async (firstName, middleName, lastName) => connection.execute(
    'INSERT INTO model_example.authors (first_name, middle_name, last_name) VALUES (?,?,?)',
    [firstName, middleName, lastName],
);
module.exports = {
    getAll,
    findById,
    isValid,
    create
};
// O model Author exporta uma função getAll . Essa função retornará todos os escritores cadastrados no banco de dados. Utilizamos o método execute para fazer uma query mysql como já estamos acostumados. Esse método retorna uma Promise que quando resolvida, nos fornece um array com 2 campos: [rows, fields] . O primeiro index é onde está a resposta que desejamos (no caso o Authors) e no segundo vêm algumas informações extras sobre a query que não iremos utilizar.

// Repare que função getAll faz o mapeamento dos dados do banco para a aplicação, convertendo os nomes de snake_case para camelCase , utilizando a função serialize . Note também o uso da função getNewAuthor , que formata os dados para que seja exibido o nome completo do autor em uma única string.
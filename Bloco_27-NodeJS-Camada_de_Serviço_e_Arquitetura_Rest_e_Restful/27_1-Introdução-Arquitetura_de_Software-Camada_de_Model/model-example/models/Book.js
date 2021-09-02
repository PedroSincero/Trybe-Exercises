// models/Author.js

const connection = require('./connection');

// Cria uma string com o nome completo do autor

// const getNewAuthor = (bookData) => {
// const { id, title } = bookData;

// return {
//     id,
//     title,
// };
// };

// Converte o nome dos campos de snake_case para camelCase

const serialize = ({id, title, author_id}) => ({
  id,
  title,
  authorId: author_id,
});

// Busca todos os autores do banco.

const getAllBooks = async () => {
  const [books] = await connection.execute(
    'SELECT * FROM model_example.books;',
  );
  return books.map(serialize);
};

const findByBookId = async (id) => {
  const query = 'SELECT * FROM model_example.books WHERE id = ?';
  const [bookData] = await connection.execute(query, [id]);

  if(bookData.length === 0) return null;

  return bookData.map(serialize)
}

module.exports = {
  getAllBooks,
  findByBookId
};
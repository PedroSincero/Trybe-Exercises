// models/Author.js

const connection = require('./connection');
const Author = require('./Author');
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

const isValidBook = async (title, author_id) => {
  if(!title || typeof title !== 'string' || title < 3) return false;
  if(!author_id || typeof author_id !== 'number' || !(await Author.findById(author_id))) return false;
  return true;
};

const createBook = async (title, author_id) => {
  connection.execute(
    'INSERT INTO model_example.books (title, author_id) VALUES (?,?)', [title, author_id]
  );
}
module.exports = {
  getAllBooks,
  findByBookId,
  isValidBook,
  createBook
};

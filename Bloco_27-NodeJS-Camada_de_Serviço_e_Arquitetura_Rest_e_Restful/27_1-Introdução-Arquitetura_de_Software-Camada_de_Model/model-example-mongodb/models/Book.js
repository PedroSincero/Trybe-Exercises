const connection = require('./connection');
const { ObjectId } = require('mongodb');

const serialize = ({id, title, author_id}) => ({
  id,
  title,
  authorId: author_id,
});


const getAllBooks = async () => {
  const connections = await connection();
  const findConnect = await connections.collection('books').find().toArray();
  const result = findConnect.map(serialize);

  return result;
};


const findByBookId = async (id) => {
  const connections = await connection();
  const findConnect = await connections.collection('books').findOne( new ObjectId(id) );

  if(!findConnect) return null;

  return serialize(findConnect);
}

const createBook = async (title, author_Id) => {
  const connections = await connection();
  const insertConnect = await connections.collection('books').insertOne({ title, author_Id });
  return insertConnect;
}

const isValidBook = async (title, author_id) => {
  if(!title || typeof title !== 'string' || title < 3) return false;
  if(!author_id || typeof author_id !== 'number' || !(await Author.findById(author_id))) return false;
  return true;
};

module.exports = {
  getAllBooks,
  findByBookId,
  isValidBook,
  createBook
};

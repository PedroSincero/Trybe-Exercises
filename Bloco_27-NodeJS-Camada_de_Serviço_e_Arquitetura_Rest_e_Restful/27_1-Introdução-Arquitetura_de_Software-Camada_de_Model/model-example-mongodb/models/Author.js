// models/Author.js
const {
  ObjectId
} = require('mongodb');

const connection = require('./connection');

// Busca todos os autores do banco.
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

// ASYNC AWAIT VERSION
const getMongoAll = async () => {
  const connections = await connection();
  const findConnect = await connections.collection('authors').find().toArray();
  const result = findConnect.map(({
    _id,
    firstName,
    middleName,
    lastName
  }) => getNewAuthor({
    id: _id,
    firstName,
    middleName,
    lastName
  }));
  return result;
}

// Busca um autor específico, a partir do seu ID
// @param {String} id ID do autor a ser recuperado

const findById = async (id) => {
  if (!ObjectId.isValid(id)) {
    return null;
  }

  const authorData = await connection()
    .then((db) => db.collection('authors').findOne(new ObjectId(id)));

  if (!authorData) return null;

  const {
    firstName,
    middleName,
    lastName
  } = authorData;

  return getNewAuthor({
    id,
    firstName,
    middleName,
    lastName
  });
};

const create = async (firstName, middleName, lastName) =>
  connection()
  .then((db) => db.collection('authors').insertOne({
    firstName,
    middleName,
    lastName
  }))
  .then(result => getNewAuthor({
    id: result.insertedId,
    firstName,
    middleName,
    lastName
  }));

const isValid = (firstName, middleName, lastName) => {
  if (!firstName || typeof firstName !== 'string') return false;
  if (!lastName || typeof lastName !== 'string') return false;
  if (middleName && typeof middleName !== 'string') return false;

  return true;
};

// ...
module.exports = {
  getMongoAll,
  findById,
  create,
  isValid,
};

// THEN CATCH VERSION
// const getMongoAll = async () => {
//   return connection()
//     .then((db) => db.collection('authors').find().toArray())
//     .then((authors) =>
//       authors.map(({
//           _id,
//           firstName,
//           middleName,
//           lastName
//         }) =>
//         getNewAuthor({
//           id: _id,
//           firstName,
//           middleName,
//           lastName,
//         })
//       )
//     );
// }
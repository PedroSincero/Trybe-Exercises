const connection = require('./connection');
const {
  ObjectId
} = require('mongodb');

const message = (body) => {
  return {
    "error": true,
    "message": `O campo ${body} está Inválido`
  }
};

// console.log(message('firstName'));

const disruption = (result) => ({ id: result.insertedId, firstName, lastName, email });

const createNewUser = async (firstName, lastName, email, password) => {
  const startMongo = await connection();
  const insertConnect = await startMongo.collection('users').insertOne({
    password,
    firstName,
    lastName,
    email,
  });
  return disruption(insertConnect);
}

const isValidUser = (req, res) => {
  const {
    firstName,
    lastName,
    email,
    password
  } = req.body;
  if (!firstName) return res.status(400).json(message('firstName'));
  if (!lastName) return res.status(400).json(message('lastName'));
  if (!email) return res.status(400).json(message('email'));
  if (typeof password !== 'string' || password.length < 6) {
    return res.status(400).json({
      "error": true,
      "message": "O campo 'password' deve ter pelo menos 6 caracteres"
    });
  }
}

module.exports = {
  createNewUser,
  isValidUser
}
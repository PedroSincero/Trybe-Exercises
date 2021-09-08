const userController = async (req, res) => {
  try {
    // ruim 😧
    await UserService.create(req);

    // bom! 😊
    const { email, password } = req.body;
    await UserService.create(email, password);

    res.send({ message: 'Tudo certo!' });
  } catch (e) {
    res.status(500).send({ message: 'Algo deu errado' });
  }
};

// O ambiente Node tem uma variável global que se chama process ; dentro dela temos um objeto env que armazena os valores de todas as variáveis de ambiente definidas no sistema operacional.
// Podemos setar variáveis de ambiente pelo terminal:

// DB_URL="mongodb://localhost:27017" node index.js

// index.js

console.log(process.env.DB_URL) // mongodb://localhost:27017

// No entanto, uma forma melhor e mais fácil, quando temos muitas variáveis, é criar um arquivo .env na raiz do projeto e usar a biblioteca dotenv , que basicamente pega o conteúdo desse arquivo e o deixa acessível via process.env .

// # .env
// PORT=3000
// DB_URL=mongodb://localhost:27017
// DB_NAME=model_example

// index.js

require('dotenv').config();
// ...

const PORT = process.env.PORT;
app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
// Server listening on port 3000

// models/connection.js
const mongoClient = require('mongodb').MongoClient;

const connection = () => {
  return mongoClient
    .connect(process.env.DB_URL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
    .then((conn) => conn.db(process.env.DB_NAME))
    .catch((err) => {
      console.error(err);
      process.exit(1);
   });
};

module.exports = connection;

// Por último, não se esqueça de colocar o .env no .gitignore , pois não vamos querer versionar esse arquivo.

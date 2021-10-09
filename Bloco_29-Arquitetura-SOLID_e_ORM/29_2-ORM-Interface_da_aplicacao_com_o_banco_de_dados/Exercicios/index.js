const express = require('express');
const bodyParser = require('body-parser');

const booksController = require('./controllers/booksController');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

app.get('/books', booksController.getAll);
app.get('/book/:id', booksController.getById);
app.post('/book', booksController.createNew);
app.post('/book/:id', booksController.updateById);
app.delete('/book/:id', booksController.deleteById);

app.listen(PORT, () => console.log(`Ouvindo na porta ${PORT}!`));

// https://mongoosejs.com/ , https://dev.to/nedsoft/performing-crud-with-sequelize-29cf , https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Express_Nodejs/mongoose , https://github.com/davesag/sequelize-test-helpers
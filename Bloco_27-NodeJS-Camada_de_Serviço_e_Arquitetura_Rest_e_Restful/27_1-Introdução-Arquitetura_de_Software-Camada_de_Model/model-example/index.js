// index.js

const express = require('express');

const Author = require('./models/Author');
const Book = require('./models/Book');
const app = express();

app.get('/authors', async (_req, res) => {
    const authors = await Author.getAll();

    res.status(200).json(authors);
});

app.get('/books', async (_req, res) => {
  const books = await Book.getAllBooks();
  res.status(200).json(books);
});

app.get('/authors/:id', async (req, res) => {
  const { id } = req.params;

  const author = await Author.findById(id);

  if (!author) return res.status(404).json({ message: 'Not found' });

  res.status(200).json(author);
});

app.get('/books/:id', async (req, res) => {
  const { id } = req.params;

  const book = await Book.findByBookId(id);

  if (!book) return res.status(404).json({ message: 'Not found'});

  return res.status(200).json(book);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
 console.log(`Ouvindo a porta ${PORT}`);
});

// A essa aplicação, adicionamos uma nova rota GET /authors . Então fazemos como já havíamos aprendido anteriormente, passamos uma função que acessa os parâmetros req e res , que chama a função getAll do nosso model , aguarda sua execução e então retorna um JSON com os dados enviados pelo banco.

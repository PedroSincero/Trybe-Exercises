// const express = require('express');
const bodyParser = require('body-parser');

// const app = express();
app.use(bodyParser.json());

// ...

// Agora vamos implementar nossa rota que vai receber dados no body da requisição.
// ...
app.post('/recipes', function (req, res) {
  const { id, name, price } = req.body;
  recipes.push({ id, name, price});
  res.status(201).json({ message: 'Recipe created successfully!'});
});

// Perceba, que repetimos a rota /recipes , só que agora usando o método .post . No Express, é possível ter rotas com o mesmo caminho desde que o método (ou verbo) HTTP utilizado seja diferente, na outra rota definimos o que acontece para o método GET . Por falar nisso, fica a pergunta, como vamos conseguir fazer requisições já que por padrão as requisições que fazemos ou no navegador ou no fetch api são do tipo GET ?
fetch(`http://localhost:3001/recipes/`, {
  method: 'POST',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    id: 4,
    title: 'Macarrão com Frango',
    price: 30
  })
});

// ...

app.post('/recipes', function (req, res) {
  const { id, name, price } = req.body;
  recipes.push({ id, name, price});
  res.status(201).json({ message: 'Recipe created successfully!'});
});

// ...

// Assim como podemos enviar informações no body da requisição, também é possível enviar informações no header da mesma. Vamos imaginar que precisamos ter uma rota que recebe um token para ser validado, a regra da validação é checar se o token possui 16 caracteres.
// ...

app.get('/validateToken', function (req, res) {
  const { id, nome, preco } = req.body;
  const token = req.headers.authorization;
  if (token.length !== 16) return res.status(401).json({message: 'Invalid Token!'})';

  res.status(200).json({message: 'Valid Token!'})
});

// ...

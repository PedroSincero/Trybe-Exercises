// 1 - Criar uma nova aplicação Express;
// 2 - Dizer ao Express que, quando uma requisição com método GET for recebida no caminho /hello , a função handleHelloWorldRequest deve ser chamada;
// 3 - Pedir ao Express que crie um servidor HTTP e escute por requisições na porta 3001;
// 4 - Ao tratar uma requisição com método GET no caminho /hello , enviar o status HTTP 200 que significa OK e a mensagem "Hello world!".
// const express = require('express');

// const app = express(); // 1

// app.get('/hello', handleHelloWorldRequest); // 2

// app.listen(3001, () => {
//   console.log('Aplicação ouvindo na porta 3001');
// }); // 3

// function handleHelloWorldRequest(req, res) {
//   res.status(200).send('Hello World!'); // 4
// }

// Estruturando uma API

/* index.js */
const express = require('express');
const app = express();

const recipes = [
  { id: 1, name: 'Lasanha', price: 40.0, waitTime: 30 },
  { id: 2, name: 'Macarrão a Bolonhesa', price: 35.0, waitTime: 25 },
  { id: 3, name: 'Macarrão com molho branco', price: 35.0, waitTime: 25 },
];

const drinks = [
  { id: 1, name: 'Refrigerante Lata', price: 5.0 },
  { id: 2, name: 'Refrigerante 600ml', price: 8.0 },
  { id: 3, name: 'Suco 300ml', price: 4.0 },
  { id: 4, name: 'Suco 1l', price: 10.0 },
  { id: 5, name: 'Cerveja Lata', price: 4.5 },
  { id: 6, name: 'Agua Mineral 500 ml', price: 5.0 },
];

app.get('/recipes', function (req, res) {
  res.json(recipes.sort((a, b) => a.name < b.name ? -1 : (a.name > b.name ? 1 : 0)));
});


app.get('/drinks', (req, res) => {
  res.json(drinks.sort((a, b) => a.name < b.name ? -1 : (a.name > b.name ? 1 : 0)));
});

app.listen(3001, () => {
  console.log('Aplicação ouvindo na porta 3001');
});

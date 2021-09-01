// 1 - Crie uma rota POST /user/register que receba uma requisição que envie username , email e password no body da requisição, onde:

// * username deve ter mais de 3 caracteres;
// * email deve ter o formato email@mail.com;
// * password deve conter no mínimo 4 caracteres e no máximo 8 (todos números);
// * Para todos os casos não atendidos acima deve ser retornado o código de status e um JSON com uma mensagem de erro, ex: status 400 e { "message": "invalid data" } ;
// * Caso tenha sucesso deve ser retornado uma resposta com o código de status e um JSON com uma mensagem de sucesso, ex: status 201 e { "message": "user created" } ;

const express = require('express');
const bodyParser = require('body-parser');
const fetch = require("node-fetch");
const postRouter = require('./postRouter');
const routerNotFound = require('./routerNotFound');
const user = require('./user');
const { isValidToken } = require('./validation');
const app = express();
app.use(bodyParser.json());

app.use('/user', user);

app.get('/btc/price', isValidToken, async (req, res) => {
const result = await fetch('https://api.coindesk.com/v1/bpi/currentprice/BTC.json');
const jsonResult = await result.json(); 
res.status(200).json(jsonResult);
});

app.use('/posts', postRouter);

app.listen(3005, () => console.log('Run server 3005'));

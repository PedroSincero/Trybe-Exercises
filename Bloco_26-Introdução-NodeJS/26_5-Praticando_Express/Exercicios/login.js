// 2 - Crie uma rota POST /user/login que receba uma requisição que envie email / password no body da requisição e devolva um token como resposta, onde:

// * O formato desse token retornado deve ser uma string aleatória com 12 caracteres;
// * O email recebido deve ter o formato email@mail.com;
// * O password deve conter no mínimo 4 caracteres e no máximo 8, todos números;
// * Para todos os casos não atendidos acima deve ser retornado o código de status e um JSON com uma mensagem de erro, ex: status 400 e { "message": "email or password is incorrect" }
// * Caso tenha sucesso deve ser retornado uma resposta com o código de status e um JSON com uma mensagem de sucesso, ex: status 200 e { "token": "86567349784e" } ;

const express = require('express');
const router = express.Router();
const { validatePassword, validateEmail } = require('./validLogin.js');

// token
  function createToken(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
  
    for (let i = 0; i < length; i+=1) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

router.post('/login', validatePassword, validateEmail, (req, res) => {
  const {
    token,
    email,
    password
  } = req.body;
  return res.status(200).json({
    token: createToken(12)
  })
});

module.exports = router;

// Agradecimentos a https://qastack.com.br/programming/1349404/generate-random-string-characters-in-javascript
// 1 - Crie uma rota POST /user/register que receba uma requisição que envie username , email e password no body da requisição, onde:
// * username deve ter mais de 3 caracteres; X
// * email deve ter o formato email@mail.com.br;
// * password deve conter no mínimo 4 caracteres e no máximo 8 (todos números);
// * Para todos os casos não atendidos acima deve ser retornado o código de status e um JSON com uma mensagem de erro, ex: status 400 e { "message": "invalid data" } ;
// * Caso tenha sucesso deve ser retornado uma resposta com o código de status e um JSON com uma mensagem de sucesso, ex: status 201 e { "message": "user created" } ;


const express = require('express');
const router = express.Router();

const validateName = (req, res, next) => {
  const { username } = req.body;
  if(!username || username.length < 4) return res.status(400).json({ message: 'Invalid Name'});
  next()
};

const validateEmail = (req, res, next) => {
  const { email } = req.body;
  const regex = /^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i;
  if(!email || !email.match(regex)) return res.status(400).json({ message: 'Invalid Email'});

  next()
};

const validatePassword = (req, res, next) => {
  const { password } = req.body;

  if(
    typeof password === 'number' ||
      `${password}`.length <= 3 || 
      `${password}`.length >= 9
    ) return res.status(400).json({ message: 'Invalid Password'});
  next()
};

router.post('/register', validateName, validateEmail,validatePassword, (req, res) => {
  const { username, email, password } = req.body;
  return res.status(201).json({ message: 'user created'})
});

module.exports = router;

// Agradecimentos: https://pt.stackoverflow.com/questions/1386/express%C3%A3o-regular-para-valida%C3%A7%C3%A3o-de-e-mail

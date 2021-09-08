const express = require('express');

const app = express();
const { getAllCep, createCep, findByCep } = require('./Cep');
const INVALID_CEP = { "error": { "code": "invalidData", "message": "CEP inválido" } };
const NOTFOUND_CEP = { "error": { "code": "notFound", "message": "CEP não encontrado" } };
const { findByCEP } = require('./controllers/controlCEP');

app.use(express.json());

app.get('/ping', (req, res) => {
  res.status(200).json({ message: 'pong!' });
});

app.get('/ceps', async (req, res) => {
  const ceps = await getAllCep();
  res.status(200).json(ceps);
})

app.get('/ceps/:cep',findByCEP);

app.post('/ceps', async (req, res) => {
  const {cep, logradouro, bairro, localidade, uf } = req.body;

  await createCep(cep, logradouro, bairro, localidade, uf);
  return res.status(200).json({ message: `O Cep: ${cep} Foi criado com Sucesso`});

});

const PORT = process.env.PORT || 3005;

app.listen(PORT, () => { console.log(`Listening on port ${PORT}`); });
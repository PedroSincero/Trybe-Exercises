const INVALID_CEP = { "error": { "code": "invalidData", "message": "CEP inválido" } };
const NOTFOUND_CEP = { "error": { "code": "notFound", "message": "CEP não encontrado" } };

const { searchDBCep } = require('../Cep');

const findByCEP = async (req, res) => {
  const { cep } = req.params;
  const findCep = await searchDBCep(cep);
  const regexp = /\d{5}-?\d{3}/;

  if(!regexp.test(cep)) return res.status(400).json(INVALID_CEP)

  if (!findCep) return res.status(400).json(NOTFOUND_CEP);

  return res.status(200).json(findCep);
}

module.exports = {
  findByCEP
}
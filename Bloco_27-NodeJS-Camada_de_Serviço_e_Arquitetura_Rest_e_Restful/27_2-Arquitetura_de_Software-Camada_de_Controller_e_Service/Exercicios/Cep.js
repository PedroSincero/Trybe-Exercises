const connection = require('./connection');

const serialize = ({cep, logradouro, bairro, localidade, uf}) => ({
  cep,
  logradouro,
  bairro,
  localidade,
  uf
});


const getAllCep = async () => {
  const [ceps] = await connection.execute(
      'SELECT * FROM cep_lookup.ceps;',
  );
  return ceps.map(serialize);
};

const createCep = async (cep, logradouro, bairro, localidade, uf) => 
  await connection.execute(
  'INSERT INTO cep_lookup.ceps (cep, logradouro, bairro, localidade, uf) VALUES (?,?,?,?,?)', [cep, logradouro, bairro, localidade, uf]
  );

const searchDBCep = async (cep) => {
  const query = 'SELECT * FROM cep_lookup.ceps WHERE cep = ?';
  const [ceps] = await connection.execute(query,[cep]);

  if (ceps.length === 0) return null;

  return ceps.map(serialize);
}

module.exports = {
  getAllCep,
  createCep,
  searchDBCep
}
// 2 - Crie uma rota GET /btc/price que receba uma requisição com um token na chave Authorization do headers da requisição e verifique se ele está correto, onde:
// * O token deve ser uma string de 12 caracteres contendo letras e/ou números.
// * Para todos os casos não atendidos acima deve ser retornado o código de status e um JSON com uma mensagem de erro, ex: status 401 e { "message": "invalid token" } ;
// * Caso tenha sucesso deve ser feito um fetch em uma API externa de sua preferência e retorne os dados da API como resposta;

const isValidToken = (req, res, next) => {
  const token = req.headers.authorization;
  const tokenRegex = /^[a-zA-Z0-9]{12}$/;

  if (!token || !tokenRegex.test(token)) {
    return res.status(401).json({ message: 'Invalid token'});
  }

  next();
}

module.exports = { isValidToken };

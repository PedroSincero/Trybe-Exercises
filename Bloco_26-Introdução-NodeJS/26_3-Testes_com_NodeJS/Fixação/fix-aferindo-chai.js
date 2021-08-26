// Vamos ver como fica nosso cenário de teste inteiro com mocha + chai :
const { expect } = require('chai');

const calculaSituacao = require('../examples/calculaSituacao');

describe('Quando a média for menor que 7', () => {
  it('retorna "reprovado"', () => {
    const resposta = calculaSituacao(4);

    expect(resposta).equals('reprovado');
  });
});

// Para tornar nosso teste ainda mais legível e elegante, o chai nos fornece outros getters encadeáveis que possuem um papel puramente estético. Por exemplo o to e o be , que nos permite escrever nossa assertion da seguinte maneira:
const { expect } = require('chai');

const calculaSituacao = require('../examples/calculaSituacao');

describe('Quando a média for menor que 7', () => {
  it('retorna "reprovado"', () => {
    const resposta = calculaSituacao(4);

    expect(resposta).to.be.equals('reprovado');
  });
});
// Perceba que o to e o be não alteraram em nada a validação realizada, porém, a leitura fica muito mais fluída e natural, é como se estivéssemos dito que nosso teste "espera a resposta ser igual a "reprovado".

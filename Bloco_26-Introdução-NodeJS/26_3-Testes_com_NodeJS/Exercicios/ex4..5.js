// Descreva todos os cenários de teste utilizando describes ;
// Descreva todos os testes que serão feitos utilizando its ;
// Crie as asserções validando se o retorno da função possui o valor e tipo esperado.
const fs = require('fs');
const { expect } = require('chai');
const sinon = require('sinon');
const func = require('./func');

describe('Executa a função func', () => {
  describe('a resposta', () => {
    before(() => {
      sinon.stub(fs, 'writeFileSync')
    });
    after(() => {
      fs.writeFileSync.restore();
    });

    it('é uma "string"', () => {
      const resposta = func('arquivo.txt', '#vqv conteúdo');

      expect(resposta).to.be.a('string');
    });

    it('é igual a "ok"', () => {
      const resposta = func('arquivo.txt', '#vqv conteúdo');

      expect(resposta).to.be.equals('ok');
    });
  });
});
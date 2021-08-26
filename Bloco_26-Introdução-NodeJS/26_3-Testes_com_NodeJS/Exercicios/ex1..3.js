const { expect } = require('chai');

const numb = require('./numb');

// 1.1 Descreva todos os cenário de teste utilizando describes ;
describe('1- Testando Função "numb"', () => {
  // 1.2 Descreva todos os testes que serão feitos utilizando its ;
  // 1.3 Crie as asserções validando se os retornos de cada cenário tem o tipo e o valor esperado.
  it('1.1 - numb Retorna uma String ?', () => {
    const result = numb(10)
    expect(result).to.be.a('string')
  });
  it('1.2 - ao colocar uma String, numb retorna uma mensagem de erro escrito "o valor deve ser um número" ?', () => {
    const result = numb('bobo')
    expect(result).to.be.equal("o valor deve ser um número")
  });
  it('1.3 - Ao colocar um numero positivo, numb retorna string "positivo" ?', () => {
    const result = numb(5)
    expect(result).to.be.equal('positivo')
  });
  it('1.4 - Ao colocar um numero neutro,numb retorna string "neutro" ?', () => {
    const result = numb(0)
    expect(result).to.be.equal('neutro')
  });
  it('1.5 - Ao colocar um numero negativo, numb retorna string "negativo" ?', () => {
    const result = numb(-5)
    expect(result).to.be.equal('negativo')
  });
})


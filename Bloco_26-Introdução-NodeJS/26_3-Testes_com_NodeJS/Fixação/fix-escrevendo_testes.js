// Relembrando os testes que escrevemos "na mão", o mocha substitui aqueles logs que utilizamos para descrever cada teste:
console.log('Quando a média for maior que 7, retorna "aprovado":');

// Bora ver na prática como podemos fazer isso com a ajuda do mocha . Esse mesmo cenário 1 , utilizando describe para descrever o cenário ficaria assim:
describe('Quando a média for menor que 7', () => {
  //
});

// Descrito nosso comportamento, vamos adicionar o que será testado de fato, ou seja, o que é esperado. Para isso, temos o it :
describe('Quando a média for menor que 7', () => {
  it('retorna "reprovado"', () => {
    //
  });
});

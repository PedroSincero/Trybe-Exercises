// 1. crie uma nova pasta e, dentro dela, crie um pacote Node.js com o npm init chamado my-scripts . Realize os exercícios dentro desse pacote.
// Crie um script para calcular o Índice de Massa Corporal(IMC) de uma pessoa.
const readline = require('readline-sync');

// const name = readline.question('What is your name? ');
const peso = readline.questionFloat('Qual é o seu peso ?');
const altura = readline.questionInt('Qual é a sua Altura ?')
const imc = (peso / Math.pow(altura / 100, 2)).toFixed(2)
// console.log(`Olá, ${name}! O seu IMC é de ${(peso / Math.pow(altura, 2).toFixed(2))}`);
// 2. Vamos sofisticar um pouco mais nosso script. Além de imprimir o IMC na tela, imprima também em qual categoria da tabela abaixo aquele IMC se enquadra:

switch (true) {
  case (imc < 18.5):
    console.log('Abaixo do peso (magreza)');
    break;
  case (imc >= 18.5 && imc < 25):
    console.log('Peso normal ');
    break;
  case (imc >= 25.0 && imc < 29.9):
    console.log('Acima do peso (sobrepeso)');
    break;
  case (imc >= 30.0 && imc < 34.9):
    console.log('Obesidade grau I');
    break;
  case (imc >= 35.0 && imc < 39.9):
    console.log('Obesidade grau II');
    break;
  case (imc > 40): 
    console.log('Obesidade grau III e IV');
    break;
  default:
    console.log('sinto muito mas não encontramos o seu imc');
}
// console.log(`IMC: ${imc}`)


// 3. Vamos criar mais um script. Dessa vez, para calcular a velocidade média de um carro numa corrida.
const readline = require('readline-sync');

const distancia = readline.questionInt('Qual é a distancia ?');
const tempo = readline.questionInt('Qual é o tempo?');
const velocidadeMedia = distancia / tempo; 

console.log(`VM: ${velocidadeMedia}`);
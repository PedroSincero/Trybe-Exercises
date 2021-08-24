// Para exportar algo no sistema CommonJS, utilizamos a variável global module.exports , atribuindo a ela o valor que desejamos exportar:
// brlValue.js
const brl = 5.37;

module.exports = brl;

// No arquivo acima estamos exportando do nosso módulo o valor da constante brl , que é 5.37 . Ao importarmos esse módulo, receberíamos o valor 5.37 como resposta. Apesar de isso funcionar, exportar um único valor constante assim não é comum. Vamos observar um caso que acontece com mais frequência:

// brlValue.js
const brl = 5.37;

const usdToBrl = (valueInUsd) => valueInUsd * brl;

module.exports = usdToBrl;

// Agora estamos exportando uma função de forma que podemos utilizá-la para converter um valor em dólares para outro valor, em reais.
// index.js
const convert = require('./brlValue');

const usd = 10;
const brl = convert(usd);

console.log(brl) // 53.7

// Suponhamos agora que seja desejável exportar tanto a função de conversão quanto o valor do dólar (a variável brl ). Para isso, podemos exportar um objeto contendo as duas constantes da seguinte forma:
// brlValue.js
const brl = 5.37;

const usdToBrl = (valueInUsd) => valueInUsd * brl;

module.exports = {
  brl,
  usdToBrl,
};
// Dessa forma, ao importarmos o módulo, receberemos um objeto como resposta:
// index.js
const brlValue = require('./brValue');

console.log(brlValue); // { brl: 5.37, usdToBrl: [Function: usdToBrl] }

console.log(`Valor do dólar: ${brlValue.brl}`); // Valor do dólar: 5.37
console.log(`10 dólares em reais: ${brlValue.usdToBrl(10)}`); // 10 dólares em reais: 53.7

// Por último, como estamos lidando com um objeto, podemos utilizar object destructuring para transformar as propriedades do objeto importado em constantes no escopo global:
const { brl, usdToBrl } = require('./brValue');

console.log(`Valor do dólar: ${brl}`); // Valor do dólar: 5.37
console.log(`10 dólares em reais: ${usdToBrl(10)}`); // 10 dólares em reais: 53.7

// Além de importarmos um arquivo como módulo, podemos importar uma pasta. Isso é útil, pois muitas vezes um módulo está dividido em vários arquivos, mas desejamos importar todas as suas funcionalidades de uma vez só. Nesse caso, a pasta precisa conter um arquivo chamado index.js , que importa cada um dos arquivos do módulo e os exporta da forma mais conveniente.
// meuModulo/funcionalidade-1.js

module.exports = function () {
  console.log('funcionalidade1');
}
// meuModulo/funcionalidade-2.js

module.exports = function () {
  console.log('funcionalidade2');
}
// meuModulo/index.js
const funcionalidade1 = require('./funcionalidade-1');
const funcionalidade2 = require('./funcionalidade-2');

module.exports = { funcionalidade1, funcionalidade2 };

// Uma vez que importamos um pacote, podemos utilizá-lo no nosso código como uma variável, dessa forma:
const fs = require('fs');

fs.readFileSync('./meuArquivo.txt');

// npm init -y

// Gabarito >> Refazer sozinho depois

const readline = require('readline-sync');

// Criamos uma lista dos scripts disponíveis
// Utilizamos objetos com `name` e `script` para facilitar a criação da lista que será exibida
const scripts = [
  { name: 'Calcular IMC', script: './imc.js' },
  { name: 'Calcular velocidade média', script: './velocidade.js' },
  { name: 'Jogo de adivinhação', script: './sorteio.js' },
];

// Iteramos sobre os scripts para criar a lista numerada
let mensagem = scripts
  .map((script, index) => `${index + 1} - ${script.name}`);
 
// Adicionamos uma linha a mais no começo da mensagem
mensagem.unshift('Escolha um número para executar o script correspondente');

// Juntamos todos os elementos em uma string, separando-os por uma quebra de linha
mensagem = mensagem.join('\n');

const scriptNumber = readline.questionInt(mensagem) - 1;

const script = scripts[scriptNumber];

if (!script) return console.log('Número inválido. Saindo');

// Chamamos o script selecionado
// Note que, no dia a dia, é mais comum utilizarmos outras formas de executar arquivos externos
// No entanto, para fins didáticos, o `require` nos atende por enquanto.
require(script.script);
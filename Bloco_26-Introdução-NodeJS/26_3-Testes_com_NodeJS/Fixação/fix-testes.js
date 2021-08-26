// O primeiro passo que precisamos dar é pensar na estrutura da nossa função:
// Quantos e quais parâmetros ela irá esperar?
// Qual tipo de resposta ela irá retornar?
// No nosso caso nossa função deverá receber um parâmetro "media" e responder com "reprovado" ou "aprovado".
// Tendo em mente esses questionamentos poderíamos simplesmente já partir para a implementação e chegar ao seguinte código:
function calculaSituacao(media) {
  if (media > 7) {
    return 'aprovado';
  }

  return 'reprovado';
}

module.exports = calculaSituacao;
// Simples né? Agora vamos testar essa função de acordo com os comportamentos que ela deveria ter segundo a proposta, nesse caso precisamos garantir que:
// Se passado um valor menor que 7 , por exemplo 4 , a resposta deve ser "reprovado" ;
// Se passado um valor maior que 7 , por exemplo 9 , a resposta ser "aprovado" ;
// E, não podemos esquecer do "OU", sendo assim, se passado 7 , a resposta deve ser "aprovado" ;
// Para validar esses cenários que pensamos podemos escrever algumas chamadas a nossa função:
const calculaSituacao = require('./examples/calculaSituacao');

console.log('Quando a média for menor que 7, retorna "reprovado":');

const respostaCenario1 = calculaSituacao(4);
if (respostaCenario1 === 'reprovado') {
  console.log(`Ok 🚀`);
} else {
  console.error('Resposta não esperada 🚨');
}
// console:
// Quando a média for menor que 7, retorna "reprovado":
// Ok 🚀

console.log('Quando a média for maior que 7, retorna "aprovado":');

const respostaCenario2 = calculaSituacao(9);
if (respostaCenario2 === 'aprovado') {
  console.log(`Ok 🚀`);
} else {
  console.error('Resposta não esperada 🚨');
}
// console:
// Quando a média for maior que 7, retorna "aprovado":
// Ok 🚀

console.log('Quando a média for igual a 7, retorna "aprovado":');

const respostaCenario3 = calculaSituacao(7);
if (respostaCenario3 === 'aprovado') {
  console.log(`Ok 🚀`);
} else {
  console.error('Resposta não esperada 🚨');
}
// console:
// Quando a média for igual a 7, retorna "aprovado":
// Resposta não esperada 🚨
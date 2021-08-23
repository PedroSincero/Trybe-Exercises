const readline = require('readline-sync');

function sorteio (resposta, aleatorio) {
  if(resposta === aleatorio){
    return console.log('Parabéns, número correto!')
  } else {
    return console.log(`Opa, não foi dessa vez. O número era ${aleatorio}`)
  }
}

function reSorteio () {
const aleatorio = Math.floor(Math.random() * 10);
const resposta = readline.questionInt('Qual é o numero?');

sorteio(resposta, aleatorio);

const novamente = readline.question('Quer jogar novamente?(Digite s para sim, e qualquer outra coisa para não)');

if(novamente === 'sim'){
  return   reSorteio();
}else {
  console.log('até o/')
  }
}
reSorteio();

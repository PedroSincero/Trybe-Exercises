const readline = require('readline-sync');

const choices = ['imc', 'velocidade', 'loteria'];

const useChoice = readline.keyInSelect(choices, 'Escolha o arquivo:');

switch (useChoice) {
  case choices.indexOf('imc'):
    const imc = require('./imc');
  case choices.indexOf('velocidade'):
    const velocidade = require('./velocidade');
  case choices.indexOf('loteria'):
    const loteria = require('./loteria');
}

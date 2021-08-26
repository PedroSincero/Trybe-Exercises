// Agora vamos ver na prática como podemos criar um stub para a função de leitura do fs :
const fs = require('fs');
const sinon = require('sinon');

sinon.stub(fs, 'readFileSync')
  .returns('Valor a ser retornado');
  
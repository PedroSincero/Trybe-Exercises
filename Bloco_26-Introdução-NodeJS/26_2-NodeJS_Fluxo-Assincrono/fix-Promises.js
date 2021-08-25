// Exemplo 1: Tratando erros de forma síncrona.
function dividirNumeros(num1, num2) {
  if (num2 == 0) throw new Error("Não pode ser feito uma divisão por zero");

  return num1 / num2;
}

try {
  const resultado = dividirNumeros(2, 1);
  console.log(`resultado: ${resultado}`);
} catch (e) {
  console.log(e.message);
}
// Exemplo 2: Tratando erros de forma assíncrona.
function dividirNumeros(num1, num2) {
  const promise = new Promise((resolve, reject) => {
    if (num2 == 0) reject(Error("Não pode ser feito uma divisão por zero"));

    const resultado = num1 / num2;
    resolve(resultado)
  });

  return promise;
}

dividirNumeros(2, 1)
  .then(result => console.log(`sucesso: ${result}`))
  .catch(err => console.log(`erro: ${err.message}`));

// Estrutura
const p = new Promise((resolve, reject) => {
  // Aqui é onde vamos realizar a lógica que precisamos
  // para "tentar cumprir" a promessa
});

// Feito isso, o próximo passo é escrever o código que, de fato, resolve a Promise. Já combinamos que nossa função promete ler um arquivo. Então, agora, vamos colocar dentro da função executor o código que busca resolver essa promessa:
const fs = require('fs');

function readFilePromise (fileName) {
  return new Promise((resolve, reject) => {

    fs.readFile(fileName, (err, content) => {
      if (err) return reject(err);
      resolve(content);
    });

  });
}


// Vamos a um exemplo de como podemos consumir a Promise que estamos retornando da nossa função logo acima:
// ...

readFilePromise('./file.txt') // A função me promete que vai ler o arquivo
  .then((content) => { // Caso ela cumpra o que prometeu
    console.log(`Lido arquivo com ${content.byteLength} bytes`); // Escrevo o resultado no console
  })
  .catch((err) => { // Caso ela não cumpra o que prometeu
    console.error(`Erro ao ler arquivo: ${err.message}`); // Escrevo o erro no console
  });

  // Para demonstrar isso, e como Promises tornam o código mais legível, vamos reescrever o código que nos levou ao callback hell mas, dessa vez, utilizando Promises:
  const fs = require('fs');

  function readFilePromise (fileName) {
    return new Promise((resolve, reject) => {
      fs.readFile(fileName, (err, content) => {
        if (err) return reject(err);
        resolve(content);
      });
    });
  }
  
  readFilePromise('file1.txt') // A função me promete que vai ler o arquivo
    .then((content) => { // Caso arquivo 1 seja lido,
      console.log(`Lido file1.txt com ${content.byteLength} bytes`); // Escrevo o resultado no console
      return readFilePromise('file2.txt'); // Chamo novamente a função, que me retorna uma nova Promise
    })
    .then(content => { // Caso a Promise retornada pelo `then` anterior seja resolvida,
      console.log(`Lido file2.txt com ${content.byteLength} bytes`); // Escrevemos o resultado no console
      return readFilePromise('file3.txt'); // E chamamos a função novamente, recebendo uma nova promessa
    })
    .then((content) => { // Caso a promessa de leitura do `file3.txt` seja resolvida,
      console.log(`Lido file3.txt com ${content.byteLength} bytes`); // Logamos o resultado no console
    })
    .catch((err) => { // Caso qualquer uma das promessas ao longo do caminho seja rejeitada
      console.log(`Erro ao ler arquivos: ${err.message}`); // Escrevemos o resultado no console
    });
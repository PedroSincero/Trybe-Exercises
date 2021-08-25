// O resultado de usarmos async / await é que o código fica com uma sintaxe quase idêntica à sintaxe utiliada para código síncrono. Veja como fica o exemplo anterior utilizando async/await :
const fs = require('fs/promises');

async function main() {
  try {
    await fs.writeFile('./meu-arquivo.txt', 'Meu textão');
    console.log('Arquivo escrito com sucesso!');
  } catch (err) {
    console.error(`Erro ao escrever o arquivo: ${err.message}`);
  }
}

main()

// Ainda sobre o writeFile , você pode especificar algumas opções na escrita de arquivos passando um terceiro parâmetro opcional para os métodos writeFile e writeFileSync . A opção flag especifica como o arquivo deve ser aberto e manipulado. O padrão é 'w' , que especifica que o arquivo deve ser aberto para escrita. Se o arquivo não existir, ele é criado. Caso contrário, ele é reescrito, ou seja, tem seu conteúdo apagado antes de o novo conteúdo ser escrito. A flag 'wx' , por exemplo, funciona como 'w' , mas lança um erro caso o arquivo já exista:
const fs = require('fs').promises;

// A flag wx abre o arquivo para escrita **apenas** caso ele não exista. Caso o contrário, um erro será lançado
fs.writeFile('./meu-arquivo.txt', 'Eu estive aqui :eyes:', { flag: 'wx' })
  .then(() => {
    console.log('Arquivo salvo');
  })
  .catch((err) => {
    // Se o arquivo existir, um erro é retornado
    console.error('err');
  });

  // Leitura de Flag https://nodejs.org/api/fs.html#fs_file_system_flags


  // O Promise.all é um método da Promise que nos permite passar um array de Promises e receber, de volta, uma única Promise. Ela será resolvida com os resultados de todas as Promises, assim que todas elas forem resolvidas. Esse método também nos permite utilizar um único catch , que será chamado caso qualquer uma das Promises seja rejeitada.

  const fs = require('fs').promises;

Promise.all([
  fs.readFile('file1.txt'),
  fs.readFile('file2.txt'),
  fs.readFile('file3.txt'),
])
  .then(([file1, file2, file3]) => {
    const fileSizeSum = file1.byteLength + file2.byteLength + file3.byteLength;
    console.log(`Lidos 3 arquivos totalizando ${fileSizeSum} bytes`);
  })
  .catch((err) => {
    console.error(`Erro ao ler arquivos: ${err.message}`);
  });
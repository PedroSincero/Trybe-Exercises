// Até agora, falamos de middlewares comuns, que recebem req , res e next e tratam uma request caso tudo esteja correndo bem. Acontece que existe ainda um outro tipo de middleware: o middleware de erro .
// A diferença de um middleware de erro para um middleware comum é que a assinatura dele recebe quatro parâmetros ao invés de três, ficando assim: function (err, req, res, next) {} .
app.use(middleware1);
app.get('/', */ ... */);
app.use(function (err, req, res, next) {
  res.status(500).send(`Algo deu errado! Mensagem: ${err.message}`);
});

// É importante notar que:
// * Middlewares de erro sempre devem vir depois de rotas e outros middlewares ;
// * Middlewares de erro sempre devem receber quatro parâmetros .

// O Express utiliza a quantidade de parâmetros que uma função recebe para determinar se ela é um middleware de erro ou um middleware comum. Ou seja, mesmo que você não vá utilizar os parâmetros req , res ou next , seu middleware de erro precisa recebê-los . Você pode adicionar um underline no começo do nome dos parâmetros que não vai usar. Isso é uma boa prática e sinaliza para quem está lendo o código que aquele parâmetro não é utilizado. Por exemplo: function (err, _req, res, _next) {} .
// Também é possível encadear middlewares de erro, no mesmo esquema dos outros middlewares, simplesmente colocando-os na sequência em que devem ser executados.

app.use(function logErrors(err, _req, _res, next) {
  console.error(err.stack);
  /* passa o erro para o próximo middleware */
  next(err);
});

app.use(function (err, _req, res, _next) {
  res.status(500);
  res.json({ error: err });
});

// Vamos usar como exemplo um método que lê um arquivo baseado em um parâmetro de rota enviado na requisição. Vamos fazer isso em um arquivo separado diferente dos exemplos anteriores que fizemos até agora.
/* errorHandlerExample.js */
const express = require('express');
const fs = require('fs/promises');

const app = express();

app.get('/:fileName', async (req, res, next) => {
    try {
        const file = await fs.readFile(`./${req.params.fileName}`);
        res.send(file.toString('utf-8'));
    } catch (e) {
        next(e); 
    }
});

app.use(function (err, req, res, next) { 
  res.status(500).json({ error: `Erro: ${err.message}` });
});

app.listen(3002);
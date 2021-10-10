// const express = require('express');
// const bodyParser = require('body-parser');
const Sequelize = require('sequelize');

// const { Addresses, Employees } = require('./models');
const config = require('./config/config');

// const app = express();
// app.use(bodyParser.json());

const sequelize = new Sequelize(config.development);

// ...

app.post('/employees', async (req, res) => {
  // Primeiro iniciamos a transação
  const t = await sequelize.transaction();

  try {
    const { firstName, lastName, age, city, street, number } = req.body;

    // Depois executamos as operações
    const employee = await Employee.create(
      { firstName, lastName, age },
      { transaction: t },
    );

    await Address.create(
      { city, street, number, employeeId: employee.id },
      { transaction: t },
    );

    // Se chegou até essa linha, quer dizer que nenhum erro ocorreu.
    // Com isso, podemos finalizar a transação usando a função `commit`.
    await t.commit();

    return res.status(201).json({ message: 'Cadastrado com sucesso' });
  } catch (e) {
    // Se entrou nesse bloco é porque alguma operação falhou.
    // Nesse caso, o sequelize irá reverter as operações anteriores com a função rollback, não sendo necessário fazer manualmente
    await t.rollback();
    console.log(e.message);
    res.status(500).json({ message: 'Algo deu errado' });
  }
});
// ...
// ...
app.post('/employees', async (req, res) => {
  try {
    const { firstName, lastName, age, city, street, number } = req.body;

    const result = await sequelize.transaction(async (t) => {
      const employee = await Employee.create({
        firstName, lastName, age
      }, { transaction: t });

      await Address.create({
        city, street, number, employeeId: employee.id
      }, { transaction: t });

      return res.status(201).json({ message: 'Cadastrado com sucesso' });
    });

    // Se chegou até aqui é porque as operações foram concluídas com sucesso,
    // não sendo necessário finalizar a transação manualmente.
    // `result` terá o resultado da transação, no caso um empregado e o endereço cadastrado
  } catch (e) {
    // Se entrou nesse bloco é porque alguma operação falhou.
    // Nesse caso, o sequelize irá reverter as operações anteriores com a função rollback, não sendo necessário fazer manualmente
    console.log(e.message);
    res.status(500).json({ message: 'Algo deu errado' });
  }
});
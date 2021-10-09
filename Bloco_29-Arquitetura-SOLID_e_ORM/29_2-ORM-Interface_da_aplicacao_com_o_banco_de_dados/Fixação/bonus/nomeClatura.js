// migrations/[timestamp]-create-user.js
// Alterando de Camel Case para Sneak Case

// module.exports = {
//   up: async (queryInterface, Sequelize) => {
//     await queryInterface.createTable('Users', {
//       id: {
//         allowNull: false,
//         autoIncrement: true,
//         primaryKey: true,
//         type: Sequelize.INTEGER,
//       },
//       fullName: {
//         type: Sequelize.STRING,
//       },
//       email: {
//         type: Sequelize.STRING,
//       },
//       createdAt: {
//         allowNull: false,
//         type: Sequelize.DATE,
field: 'created_at', // a coluna será criada no banco com este nome
//       },
//       updatedAt: {
//         allowNull: false,
//         type: Sequelize.DATE,
           field: 'updated_at', // a coluna será criada no banco com este nome
//       }
//     });
//   },

//   down: async (queryInterface, Sequelize) => {
//     await queryInterface.dropTable('Users');
//   }
// };

// seeders/[timestamp]-users.js


module.exports = {
//   up: async (queryInterface, Sequelize) => queryInterface.bulkInsert('Users',
//     [
//       {
//         fullName: 'Leonardo',
//         email: 'leo@test.com',
            // com a mudança no nome das colunas, precisamos colocar no seed o formato correspondente a este novo nome
            created_at: Sequelize.literal('CURRENT_TIMESTAMP'),
            updated_at: Sequelize.literal('CURRENT_TIMESTAMP'),
//       },
//       {
//         fullName: 'JEduardo',
//         email: 'edu@test.com',
            created_at: Sequelize.literal('CURRENT_TIMESTAMP'),
            updated_at: Sequelize.literal('CURRENT_TIMESTAMP'),
//       },
//     ], {}),

//   down: async (queryInterface) => queryInterface.bulkDelete('Users', null, {}),
// };

// Porém, como isso ficará no model . Confira o exemplo abaixo:


// const User = (sequelize, DataTypes) => {
//   const User = sequelize.define('User', {
//     fullName: DataTypes.STRING,
//     email: DataTypes.STRING,
phoneNum: DataTypes.STRING,
//   },
     {
       underscored: true,
       tableName: 'Users',
     });

//   return User;
// };

// module.exports = User;
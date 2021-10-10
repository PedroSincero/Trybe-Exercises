// No caso dos relacionamentos 1:N , não há grande diferença na maneira como criamos as associações. Caso cada employee possuísse vários address , bastaria declarar seu model da seguinte forma:

// models/Employee.js
// module.exports = (sequelize, DataTypes) => {
//   const Employee = sequelize.define('Employee', {
//     id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
//     firstName: DataTypes.STRING,
//     lastName: DataTypes.STRING,
//     age: DataTypes.INTEGER,
//   },
//   {
//     timestamps: false,
//     tableName: 'Employees',
//     underscored: true,
//   });

//   Employee.associate = (models) => {
  Employee.hasMany(models.Address,
    { foreignKey: 'employee_id', as: 'addresses' });
//   };

//   return Employee;
// };
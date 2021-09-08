const express = require('express');

const {isValidUser, createNewUser} = require('./models/User');
// const Book = require('./models/Book');
const app = express();
app.use(express.json());

app.post('/user',isValidUser, async (req, res) => {
  const { firstName, lastName, email, password } = req.body;

  const result = await createNewUser(firstName, lastName, email, password);

  return res.status(201).json({message: 'funciona, passar bem'});

});

app.get('/user', );

const PORT = process.env.PORT || 3001;

app.listen(PORT, () => {
 console.log(`Ouvindo a porta ${PORT}`);
});

// Além dos métodos GET E POST , o HTTP também possui os métodos PUT e DELETE que são convencionalmente utilizados para rotas que, respectivamente, editam e removem objetos. O Express tem métodos específicos para definir rotas para esses dois verbos. Vamos começar dando um exemplo do uso do PUT .
// ...

app.put('/recipes/:id', function (req, res) {
  const { id } = req.params;
  const { name, price } = req.body;
  const recipeIndex = recipes.findIndex((r) => r.id === parseInt(id));

  if (recipeIndex === -1) return res.status(404).json({ message: 'Recipe not found!' });

  recipes[recipeIndex] = { ...recipes[recipeIndex], name, price };

  res.status(204).end();
});
// ...

// Como utilizamos o .end() no nosso callback da rota PUT /recipes/:id não retornamos nada, apenas o status 204, que indica que a requisição foi completada com sucesso.
// Agora é a vez de implementarmos uma rota que permita remover receitas da nossa lista. Para isso vamos criar uma rota para requisições do tipo DELETE no caminho /recipes/:id .
//...

app.delete('/recipes/:id', function (req, res) {
  const { id } = req.params;
  const recipeIndex = recipes.findIndex((r) => r.id === parseInt(id));

  if (recipeIndex === -1) return res.status(404).json({ message: 'Recipe not found!' });

  recipes.splice(recipeIndex, 1);

  res.status(204).end();
});

//...

// No front-end, para fazer requisições do tipo PUT e DELETE através do fetch api podemos utilizar os exemplos de código abaixo:
// Requisição do tipo PUT
fetch(`http://localhost:3001/recipes/2`, {
  method: 'PUT',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'Macarrão ao alho e óleo',
    price: 40
  })
});

// Requisição do tipo DELETE
fetch(`http://localhost:3001/recipes/4`, {
  method: 'DELETE',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  }
});

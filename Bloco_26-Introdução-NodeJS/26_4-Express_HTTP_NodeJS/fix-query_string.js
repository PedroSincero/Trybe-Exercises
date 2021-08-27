// Para nosso exemplo, vamos definir uma rota /pratos/pesquisar?nome=Macarrão que permita, inicialmente, buscar uma lista de receitas filtrando pelo nome. Vamos usar o código abaixo.
// ...

app.get('/recipes/search', function (req, res) {
  const { name } = req.query;
  const filteredRecipes = recipes.filter((r) => r.name.includes(name));
  res.status(200).json(filteredRecipes);
});


// app.get('/recipes/:id', function (req, res) {
//  const { id } = req.params;
//  const recipe = recipes.find((r) => r.id === parseInt(id));
//  if (!recipe) return res.status(404).json({ message: 'Recipe not found!'});
//
//  res.status(200).send(recipe);
// });

// ...

// Vamos agora refatorar nosso código para que ele também seja capaz de filtrar pelo preço máximo passando um segundo parâmetro através da query string.
// ...

app.get('/prices/search', function (req, res) {
  const { name, maxPrice } = req.query;
  const filteredRecipes = recipes.filter((r) => r.name.includes(name) && r.price < parseInt(maxPrice));
  res.status(200).json(filteredRecipes);
})

// ...
# Exercício 2 Faça uma requisição ao recurso usuários da API do Github ( https://api.github.com/users ), exibindo o username e url de todos os usuários retornados.
# login / url
import requests

response = requests.get("https://api.github.com/users")
result = response.json()
print(result[0]["login"])

for user in result:
  print(user['login'], user['url'])
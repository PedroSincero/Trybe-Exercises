# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" .
# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.
def maior_nome(nomes):
  maior_nome = nomes[0]
  for nome in nomes:
    if len(nome) > len(maior_nome):
      maior_nome = nome
  return maior_nome

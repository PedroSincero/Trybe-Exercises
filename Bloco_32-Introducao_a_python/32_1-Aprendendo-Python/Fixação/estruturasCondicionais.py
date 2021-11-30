# Em uma análise de dados sobre pessoas desenvolvedoras, temos uma base de dados que contém o salário de várias pessoas, porém não temos informação da senioridade das mesmas. Para fazer um agrupamento por senioridade precisamos criar uma nova coluna que será baseada no salário.
# Caso o salário seja menor que "R$2.000,00", a pessoa será considerada como estagiária, para salários entre R$2.000,00 e R$5.800,00 júnior, entre R$5.800,00 e R$7.500,00 pleno, entre R$7.500,00 e R$10.500,00 será sênior e qualquer valor acima disto consideraremos líder.
salary = 3500
position = ""
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"
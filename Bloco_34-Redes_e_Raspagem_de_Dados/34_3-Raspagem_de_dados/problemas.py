import requests
import time

for _ in range(15):
  response = requests.get("https://www.cloudflare.com/rate-limit-test")
  print(response.status_code)
  time.sleep(6)

try:
  response = requests.get("https://httpbin.org/delay/10", timeout=2)
except requests.Timeout:
  response = requests.get("https://httpbin.org/delay/10", timeout=15)
finally:
  print(response.status_code)


# Rate Limit
# Muitas vezes a página de onde estamos removendo o conteúdo possui uma limitação de quantas requisições podemos enviar em um curto período de tempo, evitando assim ataques de negação de serviço.
# Isto pode nos levar a ficarmos bloqueados por um curto período de tempo ou até mesmo banidos de acessar um recurso.
# Que tal vermos um exemplo?
import requests


# À partir da décima requisição somos bloqueados de acessar o recurso
# Código de status 429: Too Many Requests
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response.status_code)

# Uma boa prática é sempre colocarmos um uma pausa entre as requisições, ou lote delas, mesmo que o website, onde a informação está, não faça o bloqueio, assim evitamos tirar o site do ar.
import requests
import time


# Coloca uma pausa de 6 segundos a cada requisição
# Obs: este site de exemplo tem um rate limit de 10 requisições por minuto
for _ in range(15):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(response)
    time.sleep(6)

# Timeout

# Ás vezes pedimos um recurso ao servidor, mas caso o nosso tráfego de rede esteja lento ou tenha um problema interno do servidor, nossa resposta pode demorar ou até mesmo ficar travada indefinidamente.
# Como garantir, após um tempo, que o recurso seja retornado? 🤔
import requests

# Por 10 segundos não temos certeza se a requisição irá retornar
response = requests.get("https://httpbin.org/delay/10")
print(response)

# Podemos definir um tempo limite (timeout) para que, após este tempo, possamos tomar alguma atitude como por exemplo, realizar uma nova tentativa.
# Este tempo limite normalmente é definido através de experimentações e análise do tempo de resposta normal de uma requisição.

import requests


try:
    # recurso demora muito a responder
    response = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.ReadTimeout:
    # vamos fazer uma nova requisição
    response = requests.get("http://httpbin.org/delay/1", timeout=2)
finally:
    print(response.status_code)
# No exemplo acima, para efeitos didáticos, modificamos a URI do recurso, diminuindo o delay de resposta da requisição, através do timeout , porém normalmente este valor não muda.

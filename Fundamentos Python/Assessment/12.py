# 12. Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
# Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
# Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. 
# O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.

import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")

sigla = input("Insira a sigla do estado: ")

if (sigla == "GO") | (sigla == "MT") | (sigla == "MS") | (sigla == "DF"):
  for div in soup.html.body.find_all("div", "linha"):
    print(div.text)
else:
  print("Estado não pertecente ao Centro-Oeste")

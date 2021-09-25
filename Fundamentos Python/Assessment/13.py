# 13. Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
# Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
# Conte quantas vezes apareceu a palavra ladies no conteúdo da página

import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "http://brasil.pyladies.com/about"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

paragrafos = soup.find_all('p')

uma_vez = []

texto_inteiro = ""

for paragrafo in [p.text for p in paragrafos]:
  paragrafo = paragrafo.strip()
  texto_inteiro += paragrafo.lower().replace(",", "").replace(".", "") + " "

contagem_de_palavras = Counter(texto_inteiro.split(" "))
print("São", len(contagem_de_palavras.items()), "palavras no texto")

for key, value in contagem_de_palavras.items():
    if key == "ladies":
        print("A quantidade de vezes que a palavra", key , "aparece é de:", value)
    if value == 1:
        uma_vez.append(key)
        
print("-----------------------------------------------------------------------------------------------------------------------------")
print("Palavras que aparecem apenas uma vez: ", uma_vez)




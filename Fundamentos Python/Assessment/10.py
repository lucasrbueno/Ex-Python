# 10. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
# https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
# E:
# Dentre os seguintes países nórdicos: suecia, Dinamarca e Noruega, verifique: 
# No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
# Curling
# Patinação no gelo (skating)
# Esqui (skiing)
# Hóquei sobre o gelo (ice hockey)
# Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. 
# Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

import pandas
from pygame import display

url = pandas.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv")

filtro_de_ano = url['Year'] >= 2001

paises = ['SWE', 'DEN', 'NOR']

filtro_dos_esportes = (url['Sport'] == 'Skating') | (url['Sport'] == 'Ice Hockey') | (url['Sport'] == 'Skiing') |  (url['Sport'] == 'Curling')

filtro_de_medalha = url['Medal'] == 'Gold'
ouro_total_noruega = url[(url['NOC'] == 'NOR') & filtro_dos_esportes & filtro_de_medalha & filtro_de_ano]
ouro_total_suecia = url[(url['NOC'] == 'SWE') & filtro_dos_esportes & filtro_de_medalha & filtro_de_ano]
ouro_total_dinamarca = url[(url['NOC'] == 'DEN') & filtro_dos_esportes & filtro_de_medalha & filtro_de_ano]

lista_de_medalhas_noruega = list(ouro_total_noruega.shape)[0]
lista_de_medalhas_suecia = list(ouro_total_suecia.shape)[0]
lista_de_medalhas_dinamarca = list(ouro_total_dinamarca.shape)[0]

if lista_de_medalhas_noruega > lista_de_medalhas_suecia and lista_de_medalhas_noruega > lista_de_medalhas_dinamarca:
    print(f"Noruega teve mais conquistas de ouro, com {lista_de_medalhas_noruega} medalhas no quadro total")
elif lista_de_medalhas_suecia > lista_de_medalhas_noruega and lista_de_medalhas_suecia > lista_de_medalhas_dinamarca:
    print(f"Suécia teve mais conquistas de ouro, com {lista_de_medalhas_suecia} medalhas no quadro total")
else:
    print(f"Dinamarca teve mais conquistas de ouro, com {lista_de_medalhas_dinamarca} medalhas no quadro total")

# for i in paises:
#     for j in filtro_dos_esportes:
#         todas_medalhas_dos_paises = url[(url['NOC'] == i) & (url[(url['NOC'] == j)])]
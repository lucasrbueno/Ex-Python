# 8. Um palíndromo é uma string que é lida da mesma forma do início 
# para o fim e do fim para o início, por exemplo, radar, toot e madam são palíndromos. 
# Faça um algoritmo para validar se uma string é um palíndromo. *

s = "madam"

def palindromo(s): 

    if s == s[::-1]:
        return "Sim"
    else:
        return "Sim"
 
print(palindromo(s))

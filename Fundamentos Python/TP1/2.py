# 2. Faça uma função em Python que receba do usuário a 
# idade de uma pessoa em anos, meses e dias e retorne essa idade expressa em dias. 
# Considere que todos os anos têm 365 dias.

from datetime import datetime, date

ano = int(input("ano de nascimento: "))
mes = int(input("mes de nascimento: "))
dia = int(input("dia de nascimento: "))
 
def calcularIdade(ano, mes, dia):
    idade = date.now() - date(ano, mes, dia)

    return idade
     
print(calcularIdade(ano, mes, dia))


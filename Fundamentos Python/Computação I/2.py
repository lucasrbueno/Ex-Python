# Escreva uma funcao que converte numeros inteiros entre 1 e 999 para algarismos romanos. Nao converta
# o numero para uma string. Use os tres dicionarios abaixo:

UNIDADES = { 0:"" , 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX" }

DEZENAS = { 0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9:"XC" }

CENTENAS = { 0: "", 2: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8:"DCCC", 9:"CM" }

n = 999

def traduz_romano(n):
    centena = n // 100
    dezena = (n - (centena* 100)) // 10
    unidade = n - (centena* 100) - (dezena*10)
    centena, dezena, unidade
    return f"{CENTENAS[centena]}{DEZENAS[dezena]}{UNIDADES[unidade]}"

print(traduz_romano(n))
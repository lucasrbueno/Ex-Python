# 6. Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)

frases = ["eu gosto de água", "wololo aiooo", "eu corro sempre que vejo ônibus", "Sair", "eu digo: socorro um monstro!"]

frasescomeu = []

for i in frases:
    if i == "Sair":
        break
    for palavra in i.split():
        if palavra == "eu":
            print(i)


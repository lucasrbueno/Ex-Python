# 1. Usando Python, faça o que se pede (código e printscreen):
# Crie uma lista vazia;
# Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
# Imprima a lista;
# Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
# Imprima a lista modificada;
# Imprima também o tamanho da lista usando a função len();

numeros = []

numeros.extend((1, 2, 3, 4, 5))
print(numeros)

if 6 in numeros:
    numeros.remove(6)
    print("o 6 existe")
else:
    print("6 não existe")

if 3 in numeros:
    numeros.remove(3)
    print("o 3 existe")
else:
    print("3 não existe")

print(numeros)
print(len(numeros))

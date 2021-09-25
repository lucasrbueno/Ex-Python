# 7. Escreva um programa em Python que realiza operações de inclusão e remoção em listas. 
# Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
# Mostrar lista;
# Incluir elemento;
# Remover elemento;
# Apagar todos os elementos da lista.
# Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista. 
# Se a opção for a alternativa (b), seu programa deve pedir o valor do elemento a ser incluído. 
# Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido. 
# E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.

lista = [1, 2, 4]

escolha = input("escolha um função da lista\n")

def funcao(escolha):
    while escolha != "e":
        if escolha == "a":
            print(lista)
        if escolha == "b":
            incluir = int(input("insira um número para incluir\n"))
            lista.append(incluir)
        if escolha == "c":
            excluir = int(input("insira um número para excluir\n"))
            lista.remove(excluir)
        if escolha == "d":
            print("Operação concluída")
            break
        escolha = input("escolha um função da lista")

funcao(escolha)

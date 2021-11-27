import os
import socket
import pickle

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def diretorio():
    pasta_atual = os.listdir()

    lista_diretorios = []
    lista_arquivos = []

    for item in pasta_atual:
        if os.path.isfile(item):
            lista_arquivos.append(item)
        else:
            if item not in [".git", ".vscode"]:        
                lista_diretorios.append(item)

    lista_diretorios.extend(lista_arquivos)
    msg = lista_diretorios

    return msg

host = socket.gethostname()
porta = 9999

socket_servidor.bind((host, porta))

socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    msg = socket_cliente.recv(15360000)

    if '$' == msg.decode('utf-8'): 
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    elif '1' in msg.decode('utf-8'): 
        msg = pickle.dumps(diretorio())
        socket_cliente.send(msg)
        print(diretorio())
    else:
        msg = "O que quer dizer com isso? ---> " + msg.decode('utf-8') 
  
socket_servidor.close()
input("Pressione qualquer tecla para sair...")

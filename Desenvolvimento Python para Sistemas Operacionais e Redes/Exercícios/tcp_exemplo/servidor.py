import socket
PORTA = 9001

from random import randint
# from CONSTANTS import PORTA, MENSAGEM_NUMERO, MENSAGEM_COR

def gera_cor_aleatoria(addr):
    id = addr[1]
    if id % 2 == 0:
        return f"({randint(0,255)}, {0}, {0})" #vermelho
    else:
        return f"({0}, {0}, {randint(0,255)})" #azul

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_servidor.bind(("192.168.81.128", PORTA))

socket_servidor.listen()

print("Servidor de nome", "192.168.81.128", "esperando conexão na porta", PORTA)

while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg_do_cliente = socket_cliente.recv(1024)
    msg_do_cliente = msg_do_cliente.decode('utf-8')
    print(msg_do_cliente)
    socket_cliente.send("Oi, eu sou o servidor".encode('utf-8'))
    socket_cliente.close()

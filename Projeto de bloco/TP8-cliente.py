import socket, random

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
porta = 9999

socket_servidor.bind((host, porta))

socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    msg = socket_cliente.recv(1024)

    if '$' == msg.decode('utf-8'): 
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    elif '?' in msg.decode('utf-8'): 
        resp = random.randint(0,1) 
        msg = "Sim\n"
        if resp == 0: 
            msg = "Não\n"
    else:
        msg = "Ok... " + msg.decode('utf-8') 
    socket_cliente.send(msg.encode('utf-8'))
    
socket_servidor.close()
input("Pressione qualquer tecla para sair...") 

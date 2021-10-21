# Cliente
import socket, sys

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

# Tenta se conectar ao servidor
    s.connect(("192.168.81.128", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1) # Termina o programa

print("Para encerrar, digite '$'")
msg = input()

# Envia mensagem codificada em bytes ao servidor
s.send(msg.encode('utf-8'))

while msg != '$':
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    msg = input()

    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('utf-8'))
    
# Fecha conexão com o servidor
s.close()

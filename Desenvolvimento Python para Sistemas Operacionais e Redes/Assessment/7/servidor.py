import socket, psutil, pickle

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente = (socket.gethostname(), 9999)
socket_cliente.bind(cliente)

print("Servidor de nome", socket.gethostname() , "esperando conexão na porta", 9999)

while True:
    (msg, cliente) = socket_cliente.recvfrom(15360000)

    if msg.decode('utf-8') == 'escolha':
        disco = psutil.disk_usage('.')

        msg_conteudo = [round(disco.total/(1024 * 1024 * 1024), 2), round(disco.free/(1024 * 1024 * 1024), 2)]

        socket_cliente.sendto(pickle.dumps(msg_conteudo),  cliente)
import socket, psutil

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente = (socket.gethostname(), 9999)
socket_cliente.bind(cliente)

print("Servidor de nome", socket.gethostname() , "esperando conexão na porta", 9999)

while True:
    msg, cliente = socket_cliente.recvfrom(15360000)

    if msg.decode('utf-8') == 'escolha':
        disco = psutil.disk_usage('.')

        msg_conteudo = ("Informações do disco: \nMemória usada: " + str(round(disco.total/(1024 * 1024 * 1024), 2)) + "GB" 
        + "\nMemória livre: " + str(round(disco.free/(1024 * 1024 * 1024), 2)) + "GB")

        socket_cliente.sendto(msg_conteudo.encode('utf-8'), cliente)
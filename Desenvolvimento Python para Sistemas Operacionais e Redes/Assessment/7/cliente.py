import socket, pickle

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente = (socket.gethostname(), 9999)
socket_cliente.settimeout(5)

msg = 'escolha'
requisicao = 1

while (requisicao <= 5):
    socket_cliente.sendto(msg.encode('utf-8'), cliente)
    try:
        msg_conteudo, servidor = socket_cliente.recvfrom(15360000)
        memoria = pickle.loads(msg_conteudo)
        print("Informações do disco: \nMemória usada:", memoria[0], "GB","\nMemória livre:", memoria[1], "GB")
        break
    except socket.timeout:
        requisicao = requisicao + 1

socket_cliente.close()

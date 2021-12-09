import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente = (socket.gethostname(), 9999)
socket_cliente.settimeout(5)

msg = 'escolha'
requisicao = 1

while requisicao <= 5:
    socket_cliente.sendto(msg.encode('utf-8'), cliente)
    try:
        msg_conteudo, servidor = socket_cliente.recvfrom(15360000)
        print(msg_conteudo.decode('utf-8'))
        break
    except socket.timeout:
        requisicao = requisicao + 1

socket_cliente.close()

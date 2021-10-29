import socket

host = socket.gethostbyname("")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORTA = 9001
MENSAGEM = "OI eu sou cliente da Thais"
try:
    s.connect(("192.168.81.128", PORTA))
    s.send(MENSAGEM.encode("utf-8"))

    info_bytes = s.recv(1024)
    print(info_bytes.decode('ascii'))
    
    s.close()
except Exception as erro:
    print(str(erro))

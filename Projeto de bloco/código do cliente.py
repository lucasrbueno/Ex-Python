import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    s.connect(("192.168.81.128", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1) 

print("Para encerrar, digite '$'")
msg = input()

s.send(msg.encode('utf-8'))

while msg != '$':
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    msg = input()

    s.send(msg.encode('utf-8'))
    
s.close()

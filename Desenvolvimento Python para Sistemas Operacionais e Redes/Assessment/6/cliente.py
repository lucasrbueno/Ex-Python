import socket, sys, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((socket.gethostname(), 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1)

print("Para encerrar, digite '$'")
print("1 - Informacoes dos diretorios ")

msg1 = input()

s.send(msg1.encode('utf-8'))

while msg1 != '$':
    msg = s.recv(15360000)
    if (msg1 == "1"):
        lista = pickle.loads(msg)
        for i in lista:
            print(i)
        msg1 = input()
    else:
        print(msg.decode('utf-8'))
        msg1 = input()

    s.send(msg1.encode('utf-8'))

s.close()

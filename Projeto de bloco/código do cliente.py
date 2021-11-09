import socket, sys, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("192.168.81.128", 9999))
except Exception as erro:
    print(str(erro))
    sys.exit(1) 

print("Para encerrar, digite '$'")
print("1 - Informacoes do pc ")
print("2 - Informacoes dos processos")
print("3 - Informacoes dos diretorios ")
print("4 - Informacoes da rede ")

msg1 = input()

s.send(msg1.encode('utf-8'))

while msg1 != '$':
    msg = s.recv(15360000)
    if (msg1 == "3"):
        lista = pickle.loads(msg)
        for i in lista:
            print(i)
        msg1 = input()
    else:
        print(msg.decode('utf-8'))
        msg1 = input()

    s.send(msg1.encode('utf-8'))
    
s.close()



# ----------------------------------------------------------------------------------
# CÓDIGO ORIGINAL
# ----------------------------------------------------------------------------------


# import socket, sys

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:

#     s.connect(("192.168.81.128", 9998))
# except Exception as erro:
#     print(str(erro))
#     sys.exit(1) 

# print("Para encerrar, digite '$'")
# msg = input()

# s.send(msg.encode('utf-8'))

# while msg != '$':
#     msg = s.recv(1024)
#     print(msg.decode('utf-8'))
#     msg = input()

#     s.send(msg.encode('utf-8'))
    
# s.close()

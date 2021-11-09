import socket

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 5000                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')
(msg, cliente) = udp.recvfrom(1024)
print(cliente, msg.decode('ascii'))

MSG_INCIO= "Jogar"
PERGUNTAS = {
    0: {
        "pergunta": "Que cidade sediou a primeira Olimpíada da era moderna, em 1896?",
        "opcoes": [
            "1- Paris",
            "2- Londres",
            "3- Atenas",
            "4- Roma"
        ],
        "resposta": 2
    },
    1: {
        "pergunta": "Santiago é a capital de que país?",
        "opcoes": [
            "1- Chile",
            "2- Uruguai",
            "3- Argentina",
            "4- Peru"
        ],
        "resposta": 0
    },
    2: {
        "pergunta": "De que cor é a estrela na bandeira do Vietnã?",
        "opcoes": [
            "1- laranja",
            "2- Amarelo",
            "3- Vermelho",
            "4- Verde"
        ],
        "resposta": 1
    },
    3: {
        "pergunta": "Quantos lados tem um heptadecágono?",
        "opcoes": [
            "1- 9",
            "2- 13",
            "3- 14",
            "4- 17"
        ],
        "resposta": 3
    }
}

udp.close()
input('Pressione qualquer tecla para sair...')

# ------------------------------------------------------------------------------------------

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input("Entre com a mensagem:\n")
udp.sendto (msg.encode('ascii'), dest)

(msg, cliente) = udp.recvfrom(1024)
msg = msg.decode('utf-8')

if msg == MSG_INCIO:
    for chave, valor in PERGUNTAS.items():
        envia_pergunta(udp, chave, valor, cliente)
        resposta = recebe_reposta()
        print(chave, resposta)
        pontos = calcula_pontuacao(valor, resposta, pontos)

udp.close()
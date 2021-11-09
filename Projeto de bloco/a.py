def busca_arquivo_rec(nome, dir):

    lista_dir = []
    lista_resp = []
    lista_dir.append(dir)

    while lista_dir:
        dir_atual = lista_dir[0]
        l = []
        try:
            l = os.listdir(dir_atual)
        except:
            pass
        for i in l:
            arq = os.path.join(dir_atual, i)
            if os.path.isfile(arq) and i == nome:
                lista_resp.append(arq)
            elif os.path.isdir(arq):
                lista_dir.append(arq)
        lista_dir.remove(dir_atual)
    return(lista_resp)

busca_arquivo_rec()
import cpuinfo, psutil, os, time

# info = cpuinfo.get_cpu_info()

# for i in info:
#     print(i, ":", info[i])

# print(info['brand_raw'])
# print(info['arch'])
# print(info['bits'])

# print(psutil.cpu_count(logical=False))

# print(psutil.cpu_freq().current)


lista = os.listdir()
dic = {} 
for i in lista: 
    if os.path.isfile(i):
        dic[i] = []
        dic[i].append(os.stat(i).st_size) # Tamanho
        dic[i].append(os.stat(i).st_atime) # Tempo de criação
        dic[i].append(os.stat(i).st_mtime) # Tempo de modificação

titulo = '{:11}'.format("Tamanho") 
titulo = titulo + '{:27}'.format("Data de Modificação")
titulo = titulo + '{:27}'.format("Data de Criação")
titulo = titulo + "Nome"

print(titulo)

for i in dic:
    kb = dic[i][0]/1000
    tamanho = '{:10}'.format(str('{:.2f}'.format(kb)+' KB'))
    print(tamanho, time.ctime(dic[i][2]), " ", time.ctime(dic[i][1]), " ", i)

print("-------------------------------")

lista = os.listdir()
lista_arq = [] 
lista_dir = [] 
for i in lista:
    if os.path.isfile(i):
        lista_arq.append(i)
    else:
        lista_dir.append(i)

if len(lista_arq) > 0: 
    print("Arquivos:")
for i in lista_arq:
    print("\t"+i) 
    print("")
if len(lista_dir) > 0: 
    print("Diretórios:")
for i in lista_dir:
    print("\t"+i) 
    print("") 

    dic_arq = {} 
for i in lista:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1] 
        if not ext in dic_arq:
            dic_arq[ext] = []
        dic_arq[ext].append(i) 
        
for i in dic_arq:
    print("Arquivos " + i)
    for j in dic_arq[i]:
        print("\t"+j)
    print("")
    
if len(lista) > 0:
    print("Diretórios:")
    for i in lista:
        print("\t"+i)
    print("")        

lista = os.listdir()
dic_arq = {} 
lista_dir = []
for i in lista:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1] 
        if not ext in dic_arq:
            dic_arq[ext] = []
        dic_arq[ext].append(i) 
    else:
        lista_dir.append(i)

for i in dic_arq:
    print("Arquivos " + i)
    for j in dic_arq[i]:
        print("\t"+j)
    print("")
    
if len(lista_dir) > 0:
    print("Diretórios:")
    for i in lista_dir:
        print("\t"+i)
    print("")

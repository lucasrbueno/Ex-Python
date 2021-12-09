lista_arquivo = []
lista_arquivo.append(open("a.txt", "r").readlines())
lista_arquivo.append(open("b.txt", "r").readlines())

arquivoA = []
arquivoB = []

for item in range(len(lista_arquivo)):
  if item == 0:
    for jtem in lista_arquivo[item]:
      arquivoA = jtem.split(' ')
  elif item == 1:
    for jtem in lista_arquivo[item]:
      arquivoB = jtem.split(' ')

lista_arquivo.clear()

def lista_maior_menor(arquivoA, arquivoB):
  if len(arquivoA) > len(arquivoB):
    item = len(arquivoA) - len(arquivoB)
    while item != 0:
        arquivoB.append('0')
        item -= 1
  else:
    item = len(arquivoB) - len(arquivoA)
    while item != 0:
        arquivoA.append('0')
        item -= 1

  return arquivoA, arquivoB

arquivoA, arquivoB = lista_maior_menor(arquivoA, arquivoB)

def somados(arquivoA, arquivoB):
  for item in range(len(arquivoA)):
    print(arquivoA[item], " + ", arquivoB[item], " = ", int(arquivoA[item]) + int(arquivoB[item]))

somados(arquivoA, arquivoB)

# file_generators = [read_file(path) for path in arquivoA_arquivo]

# with open("totals.txt", "w+") as outFile:
#   while True:
#     try:
#       outFile.write(f"{sum([int(next(gen)) for gen in file_generators])}\n")
#       # outFile.write(somados(arquivoA_arquivo))
      
#     except StopIteration:
#       break
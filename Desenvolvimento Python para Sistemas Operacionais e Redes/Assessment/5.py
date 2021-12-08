arquivoA_arquivo = []
arquivoA_arquivo.append(open("a.txt", "r").readlines())
arquivoA_arquivo.append(open("b.txt", "r").readlines())

arquivoA = []
arquivoB = []

for item in range(len(arquivoA_arquivo)):
  if item == 0:
    for jtem in arquivoA_arquivo[item]:
      arquivoA = jtem.split(' ')
  elif item == 1:
    for jtem in arquivoA_arquivo[item]:
      arquivoB = jtem.split(' ')
arquivoA_arquivo.clear()

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
  for i in range(len(arquivoA)):
      print(arquivoA[i], " + ", arquivoB[i], " = ", int(arquivoA[i]) + int(arquivoB[i]))

somados(arquivoA, arquivoB)


  

# arquivoB = arquivoA_arquivo[1].ReadLines()
# arquivoA.split(' '), arquivoB.split(' ')

# file_generators = [read_file(path) for path in arquivoA_arquivo]



# print(lista_maior_menorA(arquivoA_arquivo))







# with open("totals.txt", "w+") as outFile:
#   while True:
#     try:
#       outFile.write(f"{sum([int(next(gen)) for gen in file_generators])}\n")
#       # outFile.write(somados(arquivoA_arquivo))
      
#     except StopIteration:
#       break
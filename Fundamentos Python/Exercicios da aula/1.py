from collections import defaultdict

frase = "O rato roeu a roupa do rei de roma"

def conta_letras(frase):
  letras = defaultdict(int)
  for letra in frase:
    letra = letra.lower()
    letras[letra] += 1
  return letras
  
print(conta_letras(frase))

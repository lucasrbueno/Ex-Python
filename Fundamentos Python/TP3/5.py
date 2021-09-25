# 5. Escreva um programa em Python que leia nomes de alunos e 
# suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. 
# O programa deve possuir uma função que indica todos os 
# alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos). 

altura = {
  "Lucas": 1.72,
  "Juan": 1.73,
  "Thelma": 1.60,
  "Pedro": 1.20,
  "Eduardo": 0.60
}

def mediaAltura(altura):
  media = sum(altura.values())/ len(altura.values())
  for i, j in altura.items():
    if j > media:      
      print(i)
  
mediaAltura(altura)
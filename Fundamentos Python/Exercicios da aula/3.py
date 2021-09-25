import requests
import pandas as pd

df = pd.read_csv('https://hemo-project.s3.amazonaws.com/data/blood-donors-all.csv')
df

for tipo in ['A_plus', 'A_minus', 'B_plus', 'B_minus', 'AB_plus',
       'AB_minus', 'O_plus', 'O_minus']:
  print(tipo, df[tipo].sum())

print("----------------------------------")

maior = 0
maior_nome =""
for tipo in ['A_plus', 'A_minus', 'B_plus', 'B_minus', 'AB_plus',
       'AB_minus', 'O_plus', 'O_minus']:
       if df[tipo].sum() > maior:
         maior = df[tipo].sum()
         maior_nome = tipo
print(maior_nome, maior)

print("----------------------------------")

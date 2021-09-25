from collections import defaultdict

paragrafo = """Afegãos protestam em cidades do Afeganistão nesta quinta-feira (19), no Dia da Independência do país, nos primeiros sinais de resistência popular à tomada do poder pelo Talibã.
Há manifestações na capital Cabul, segundo o jornal "The New York Times", nas cidades de Jalalabad e Asadabad e no distrito da província de Paktia, segundo a agência de notícias Reuters.
Afegãos comemoram em 19 de agosto a sua independência do Reino Unido, que ocupou o país até 1919."""

paragrafo = paragrafo.replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace('"', "").replace('\n', " ")

palavras = defaultdict(int)
for palavra in paragrafo.split(" "):
  palavras[palavra] += 1
print(palavras)

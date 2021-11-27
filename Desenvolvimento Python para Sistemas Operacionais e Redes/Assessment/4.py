for item in reversed(list(open('a.txt', encoding='utf8'))):
    dado = item[::-1]
    print(dado.rstrip())
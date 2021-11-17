for line in reversed(list(open('a.txt', encoding='utf8'))):
    data = line[::-1]
    print(data.rstrip())


import os

#https://www.youtube.com/watch?v=6a4m7L7juKQ

caminho_procura = input('Digite um caminho: ')
caminho_procura = caminho_procura.replace('"', '').replace("'",'').strip()

termo_procura = input('Digite um termo: ').strip()

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    
    if tamanho < kilo:
        sigla = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        sigla = 'K'
    elif tamanho < giga:
        tamanho /= mega
        sigla = 'M'
    elif tamanho < tera:
        tamanho /= giga
        sigla = 'G'
    else:
        tamanho /= peta
        sigla = 'P'
        
for root, dirs, files in os.walk(caminho_procura):
    for file in files:
            if termo_procura in file:
                    try:
                            file_abspath = os. path.join(root, file)
                            file_name, file_ext = os.path.splitext(file)
                            file_size = os.path.getsize(file_abspath)
                            file_size_f = formata_tamanho(file_size)
                            print()
                            print('Encontrei o arquivo:', file, file_size_f)
                            print('Caminho do arquivo:', file_abspath)
                            print('Nome do arquivo: ', file_name)
                            print('Extensão do arquivo:', file_ext)
                            print('Tamanho em bytes:', file_size)
                            print('Tamanho formatado:', formata_tamanho(file_size))
                    except PermissionError as e:
                            print("Sem permissão neste arquivo.")
                    except FileNotFoundError as e:
                            print("Arquivo não encontrado.")
                    except Exception as e:
                            print("Erro desconhecido:", e)
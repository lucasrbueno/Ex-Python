# Sabe-se que uma molecula de RNA mensageiro e utilizada como base para sintetizar proteınas, no
# processo denominado de traducao. Cada trinca de bases de RNA mensageiro esta relacionado com um
# aminoacido. Combinando varios aminoacidos, temos uma proteına. Com base na tabela (simplificada)
# de trincas de RNA abaixo, crie uma funcao que receba uma string representando uma molecula de RNA
# mensageiro valida, segundo essa tabela, e retorne a cadeia de amino´acidos que representam a proteına
# correspondente:

TRINCA_RNA =  {'UUU': "Phe", 'CUU': "Leu", 'UUA': "Leu", 'AAG': "Lisina", 'UCU': "Ser", 'UAU': "Tyr", 'CAA': "Gln"}

def traducao_rna(trinca):
    return "-".join([TRINCA_RNA[trinca[i:i+3]] for i in range(0, len(trinca), 3)])
print(traducao_rna('UUUUUAUCU'))

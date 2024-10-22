# 6 QUESTÃO Elabore um programa que receba uma lista de strings genérica e retorne:

# a) O elemento com mais caracteres
# b) Verifique a ocorrência de elementos repetidos
# c) A média dos tamanhos das strings na lista

words = []

while True:
    a = input('Digite uma palavra (ou "sair" para encerrar): ')
    
    if a == 'sair':
        break

    words.append(a)

print('Palavras digitadas:', words)

more_letters = max(words, key = len)
print('O elemento com mais caracteres é:', more_letters)

counter = {}

for a in words:
    if a in counter:
        counter[a] += 1
    else:
        counter[a] = 1

repeated_words = []

for item, count in counter.items():
    if count > 1:
        repeated_words.append(item)

print('Palavras repetidas:', repeated_words)

total_len = sum(len(a) for a in words)
average_len = total_len / len(words)
print('A média dos tamanhos das strings na lista é:', average_len)
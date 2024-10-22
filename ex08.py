#8 QUESTÃO Faça um programa que receba uma lista de valores ordenados de forma crescente, e receba dois valores: um
#limite inferior e um limite superior. O programa deve retornar uma sublista com valores maiores ou iguais ao limite inferior e
#menores ou iguais ao limite superior.

numbers = []

x = int(input('Defina um limite inferior de valores: '))
y = int(input('Defina um limite máximo de valores: '))

while True:

    a = int(input('Digite um numero (ou "0" para encerrar): '))
    
    if a == 0:
        break

    numbers.append(a)


num_order = sorted(numbers)
print('Números digitados:', num_order)

sublist = [num for num in num_order if x <= num <= y]

print('Valores entre', x, 'e', y, ':', sublist)
# 5 QUESTÃO. Elabore um programa que recebe um número inteiro e retorna se seu valor é par ou ímpar.

while True: 
    a = int(input('Insira um número inteiro: '))

    if a % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
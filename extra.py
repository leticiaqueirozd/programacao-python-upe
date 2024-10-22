#1
x = 2
num_par = lambda x: f'{x} é par' if x % 2 == 0 else f'{x} é ímpar'
print(num_par(x))

#2
lista1 = [0, 2, 4]
lista2 = [2, 4, 6]

lista3 = list(filter(lambda x: x in lista1, lista2))
print('Interseção:', lista3)

#3
#distancia euclidiana
#menor ou igual
x1 = 0
x0 = 7
y1 = 0
y0 = 0
r1 = 5
r0 = 3

x = (((x1 - x0)**2 + (y1 - y0)**2)**(1/2))
colisao = lambda x: f'{x} colidiu' if x <= r0 + r1 else f'{x} não colidiu'
print(colisao(x))

# #4
# nome =

# lista_consoantes = 

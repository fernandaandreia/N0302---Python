# -*- coding: utf-8 -*_

#1 - Criar uma lista que receba uma lista de valores 20 aleatórios, 
#retornar apenas o maior valor e printar em tela

#2 - criar uma lista com 10 núm aleatórios, 
#itere essa lista e printar em tela o valor do maior e menor

# import random as r

# lista = []
# i = 1

# while i <= 20:
#     lista.append(r.randrange(1, 100, 3))
#     i = i+1

# print(f'Essa lista foi gerada aleatoriamente: {lista}')

# def maior_lista(lista):
#     return max(lista, key=int)

# print (f'Maior valor é: {maior_lista(lista)}')

# def retornar_itens_estoque(setor, *args):
#     print(f'Lista salva no estoque do setor: {setor}: ')
#     for item in args:
#         print(item)

# retornar_itens_estoque('Administrativo', 'Documentos de A a Z', 'Livro Caixa', 'Computador')

# def lista_de_compra(pessoa, **kwargs):
#     fruta = kwarg.get('fruta')
#     if fruta is not None:
#         printf(f'Na lista de compras do {pessoa} há uma fruta:')

#3 - Criar uma lista com 10 números aleatórios,
#itere esta lisa e printar os valores que são ímpares e pares,

import random as r

lista = []
lista_impar = []
lista_par = []
i = 1

while i <=10:
    lista.append(r.randrange(1,100))
    i = i + 1

print (f'Esta foi a lista gerada aleatoriamente: {lista} ')

for n in lista:
    if n % 2 != 0:
        lista_impar.append(n)
    else:
        lista_par.append(n)

print (f'impares: {lista_impar}')
print (f'pares: {lista_par}')
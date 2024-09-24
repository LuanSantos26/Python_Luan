"""
enumerate - enumera iteráveis (indices) = ele cria uma ordem de numeros na sua lista.
"""

lista = ['Luan', 'Barto', 'Geraldina']
lista.append('Cassia')

#lista_enumerada = tuple(enumerate(lista, start=20))

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('For da tupla: ')
#     for valor in tupla_enumerada:
#       print(f'\t{valor}')

# for item in enumerate(lista):
#     for valor in item:
#       print(valor)

#print(next(lista_enumerada))
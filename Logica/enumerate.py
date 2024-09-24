"""
enumerate - enumera iteráveis (indices) = ele cria uma ordem de numeros na sua lista.
"""

lista = ['Luan', 'Barto', 'Geraldina']
lista.append('Cassia')

#lista_enumerada = tuple(enumerate(lista, start=20))

#print(lista_enumerada)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)



#print(next(lista_enumerada))

for tupla_enumerada in enumerate(lista):
    print('For da tupla: ')
    for valor in tupla_enumerada:
      print(f'\t{valor}')

# for item in enumerate(lista):
#     for valor in item:
#       print(valor)
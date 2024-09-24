"""
enumerate - enumera iteráveis (indices) = ele cria uma ordem de numeros na sua lista.
"""

lista = ['Luan', 'Barto', 'Geraldina']
lista.append('Cassia')

lista_enumerada = tuple(enumerate(lista))

print(lista_enumerada)

#for item in enumerate(lista):
    #print(item)



#print(next(lista_enumerada))
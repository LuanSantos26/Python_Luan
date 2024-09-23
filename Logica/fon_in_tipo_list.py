"""
for in com listas
"""
lista = ['Luan','Barto','Geraldina']
lista.append('João')
                      
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
"""
#Iterável -> str, range, etc.
#Iterador -> quem sabe entregar um valor por vez
#next -> me entregue o próximo valor
#iter -> me entregue seu iterador    
"""
# texto = 'Luan' # iteravel
'''
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

'''
# for letra in texto
# texto = 'Luan' # iteravel
# iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
 #control k + control c comenta todas as linhas selecionaveis, para descomentar utilizar o control k + control u
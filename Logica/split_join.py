"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - A funçãostrip() serve para remover os espaços em branco no início e no final de uma string,
 retornando uma cópia formatada da string sem os espaços em branco do ínicio e final.
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
#frases_unidas = ', '.join(lista_frases)
#print(frases_unidas)
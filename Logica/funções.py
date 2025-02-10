"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu codigo.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor especifico.
Por padrão, funções Python retornam None( nada)    
    
"""

def saudacao(nome='teste'):
    print(f'Olá, {nome}!')

saudacao('Luan')
saudacao('Bartolomeu')
saudacao('Geraldina')
saudacao()
#Funções podem usar parâmetros para receber valores.
# Parâmetro é o nome da "variável" dentro dos parênteses,
# argumento é o valor passado para o parâmetro no momento da execução da função.

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
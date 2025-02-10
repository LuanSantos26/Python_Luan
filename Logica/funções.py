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
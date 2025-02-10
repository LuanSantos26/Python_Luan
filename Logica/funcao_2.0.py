'''
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual ( = )
Argumento não nomeado recebe apenas o argumento ( valor )

'''
 
def soma(x, y):
    #Definiçãoda função abaixo
    print(f'{x = }  y = {y}', '|', 'x + y = ', x + y )

soma(1, 2)# 1 e 2 são considerados argumentos
soma(2, 1)
"""
Valores padrão para parametros de funções
Ao definir uma,os parametros podem ter valores padrão.
Caso o valor não seja enviado, o valor padrão sera utilizado.
Refatorar: editar o código para melhorar a legibilidade e manutenção.
"""



def soma(x, y, z=None):
    if z is not None:
        print(f'{x=}  {y=}  {z=}', x + y + z)
    else:
        print(f'{x=}  {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9,  0) 
soma(y=9, z=0, x=7)
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = (input('Digite um numero inteiro para saber se é par ou impar: '))
numero_inteiro=int(numero)
try:
    if numero_inteiro % 2 == 0:
        print(f'O numero {numero_inteiro} é par')
    else:
        numero_inteiro % 2 == 1
        print(f'O numero {numero_inteiro} é impar')
except ValueError:
    print('Você não digitou nenhum numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
."""
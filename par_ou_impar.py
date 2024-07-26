numero = (input('Digite um numero inteiro para saber se é par ou impar: '))
numero_inteiro=int(numero)
try:
    if numero_inteiro % 2 == 0:
        print(f'este numero {numero_inteiro} é par')
    else:
        numero_inteiro % 2 == 1
        print(f'este numero {numero_inteiro} é impar')
except ValueError:
    print('Você não digitou nenhum numero')
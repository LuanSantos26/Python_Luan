'''numero = (input('Digite um numero inteiro para saber se é par ou impar: '))
numero_inteiro=int(numero)
numero_str=str(numero)
try:
    if numero_inteiro % 2 == 0:
        print(f'O numero {numero_inteiro} é par')
    else:
        numero_inteiro % 2 == 1
        print(f'O numero {numero_inteiro} é impar')
except ValueError:
    if numero == str:
        print ('Você não digitou nenhum numero')
        '''
def par_ou_impar():
    try:
        numero = input('Digite um número inteiro para saber se é par ou ímpar: ')
        numero_inteiro = int(numero)

        if numero_inteiro % 2 == 0:
            print(f'O número {numero_inteiro} é par.')
        else:
            print(f'O número {numero_inteiro} é ímpar.')

    except ValueError:
        print('Você não digitou um número inteiro válido.')
        return par_ou_impar()
par_ou_impar()
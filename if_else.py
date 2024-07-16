primeiro_valor = int(input('digite um valor numerico: '))
segundo_valor = int(input('digite o segundo valor numerico: '))

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
else:
    primeiro_valor == segundo_valor
    print('Os numeros digitados são iguais !')

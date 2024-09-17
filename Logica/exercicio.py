nome =input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome  and idade  :
    print(f'seu nome é ',nome)
    print(f'seu nome de tras para frente é ',nome [::-1])
    if ' ' in nome:
        print('seu nome contem espaços.')
    else:
        print('Seu nome não contem espaços.')
    print(f'seu nome contem {len (nome)} letras')
    print(f'a primeira letra do seu nome é ',nome[0] )
    print(f'e a ultima letra do seu nome é ',nome[-1])
else:
    print('Voce não digitou nada!')
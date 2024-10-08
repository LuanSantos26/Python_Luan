"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
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

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
def horas_agora():
    try:
        horas = input('Digite que horas são agora para saber o periodo do dia: ')
        horas_inteiro = int(horas)
        if horas_inteiro <= 11:
            print(f'Bom dia são {horas_inteiro} da manhã !')
        elif horas_inteiro <= 18:
            print(f'Boa tarde são {horas_inteiro} horas da tarde !')
        else:
            horas_inteiro <= 24
            print(f'Boa noite são {horas_inteiro} horas da noite')
    except ValueError:
        print('Voce não digitou as horas e sim colocou letras ou outros caracteres.')
        return horas_agora()
horas_agora()

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
."""
def tamanho_nome():
    primeiro_nome = input("Digite seu primeiro nome: ")

    if len(primeiro_nome) <= 4:
        print("Seu nome é curto.")
    elif 5 <= len(primeiro_nome) <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")

tamanho_nome()

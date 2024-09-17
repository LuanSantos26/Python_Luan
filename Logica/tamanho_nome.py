'''
def tamanho_nome():
    primeiro_nome = input("Digite seu primeiro nome: ")

    if len(primeiro_nome) <= 4:
        print("Seu nome é curto.")
    elif 5 <= len(primeiro_nome) <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")

tamanho_nome()
'''
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
    # tenho q estudar mais
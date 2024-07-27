'''def horas_agora():
    try:
        horas = input('Digite que horas são agora para saber o periodo do dia: ')
        horas_inteiro = int(horas)
        if horas_inteiro <= 11:
            print(f'Bom dia são {horas_inteiro} da manhã !')
        elif horas_inteiro <= 17:
            print(f'Boa tarde são {horas_inteiro} horas da tarde !')
        else:
            horas_inteiro <= 24
            print(f'Boa noite são {horas_inteiro} horas da noite')
    except ValueError:
        print('Voce não digitou as horas e sim colocou letras ou outros caracteres.')
        return horas_agora()
horas_agora()
   '''

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
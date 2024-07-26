def horas_agora():
    try:
        horas = input('Digite que horas são agora para saber o periodo do dia: ')
        horas_inteiro = int(horas)
        if horas_inteiro <= 11:
            print(f'Bom dia são {horas_inteiro} horas da manhã !')
        elif horas_inteiro <= 18:
            print(f'Boa tarde são {horas_inteiro} horas da tarde !')
        else:
            horas_inteiro <= 24
            print(f'Boa noite são {horas_inteiro} horas da noite')
    except ValueError:
        print('Voce não digitou as horas e sim colocou letras ou outros caracteres.')
        return horas_agora()
horas_agora()

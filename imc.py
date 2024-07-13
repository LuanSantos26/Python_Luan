print('Ola, seja bem vindo ao calculo de IMC')
peso = (float(input('digite o peso em kilos: ')))
altura = (float(input('digite sua altura em metros: ')))
imc = (peso/(altura*altura))
print  (f'o seu calculo IMC é de: {imc:.2f} ')#o primeiro F é para concatenar string ja o segundo inbutido na variavel imc serve para formartar as casas decimais que deseja apresentar.

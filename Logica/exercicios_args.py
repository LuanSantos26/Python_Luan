#Crie uma função que fala se o numero é par ou impar e retorne dizendo se é par ou impar
def impar_ou_par ():
    input_numero = int(input("Digite um número: "))
    if input_numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")   
impar_ou_par()       

# Crie uam função que multiplica todos os argumentos não comeados recebidos
#retorne o total para uma variavel e mostre o valor da variavel
def multiplicar (*agrs):
    resultado = 1
    for numero in agrs:
        resultado *= numero
    return resultado

multiplicação = multiplicar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(multiplicação)
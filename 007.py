idade = 36
txt = "Eu sou o Gabriel e tenho {} anos de idade"
print(txt.format(idade))
# string não pode ser concatenada com numeros inteiros por isso usa esse metodo format.
quantidade = 3
item = "bolo"
valor = 14.99
meuPedido = "Eu quero {} pedaços de {} por {} reais."
meuPedido2 = "Eu quero pagar {2} reais pelos {0} pedaços de {1}."
#Esse metodo de roamatação é atribuidos por ordens das variaveis solicitadas sendo o 2 o valor, o 0 o item 
print(meuPedido.format(quantidade, item, valor))
print(meuPedido2.format(quantidade, item, valor))
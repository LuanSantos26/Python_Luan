idade = 36
txt = "Eu sou o Gabriel e tenho {} anos de idade"
print(txt.format(idade))
# string não pode ser concatenada com numeros inteiros por isso usa esse metodo format.
quantidade = 3
item = "bolo"
valor = 14.99
meuPedido = "Eu quero {} pedacos de {} por {} reais."
meuPedido2 = "Eu quero pagar {2} reais pelos {0} pedacos de {1}."
#Esse metodo de formatação é atribuidos por ordens das variaveis solicitadas sendo o 2 o valor, o 0 o item e o 1 a quantidades, só mudando a ordem solicitada dos indices.
print(meuPedido.format(quantidade, item, valor))
print(meuPedido2.format(quantidade, item, valor))
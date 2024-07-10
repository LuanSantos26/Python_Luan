txt = "Somos os chamados \"vikings\" do norte."# é usado essas barras invertidas para poder usar aspas na string sem dar erro no codigo.
print(txt)
txt = "Ola\nMundo!"#esse é usado para solicitar uma quebra de linha na string.
print(txt) 
txt = "Ola\rMundo!"#esse retorna apenas o Mundo da string.
print(txt) 
txt = "Ola\tMundo!"#utilizado para dar um espaçamento maior como se fosse um tab.
print(txt)
txt = "Isso irá inserir um \\ (barra invertida)."
print(txt) 
txt = 'It\'s alright.'
print(txt) #
txt = "Ola \bMundo!" #Este exemplo apaga um caractere (backspace):
print(txt) 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #Uma barra invertida seguida por um 'x' e um número hexadecimal representa um valor hexadecimal:
txt = "\110\145\154\154\157"
print(txt) #Uma barra invertida seguida por três inteiros resultará em um valor octal:
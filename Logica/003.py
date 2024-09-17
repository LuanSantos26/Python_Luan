D = 0 # O igual é para atribuir valor para variavel
# a == 0 # dois sinais de igual é para comparar 
print ('valor de D : ', D )
y=35e3 #Em Python, a expressão y = 35e3 representa a atribuição de um valor à variável y. Nesse caso, o valor atribuído é 35000. A notação e3 indica que o número é multiplicado por 10 elevado à terceira potência (ou seja, 10^3), resultando em 35000.
#Portanto, após essa atribuição, a variável y terá o valor 35000.

a = 'Gabriel'
b = "Seja bem vindo"
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
d = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# print(d)

e = "Ola Mundo !"

# print(e[0])

# for x in "Gabriel":
#     print(x)

# x = len(e)
# print(len(e))

txt = "Seja bem vindo ao curso de Python."

x = "vindo" in txt
print(x)
print("carro" in txt)

if "vindo" in txt:
    print("Sim, 'vindo' está presente.")

if "lucas" not in txt:
    print("'lucas' não está presente.")

x = ("incrivel")
 
def myfunc():
    x ="fantatico"
    global z #transofrma variavel local em global
    z="Bem vindo ao python"
    
    print("python é "  + x) #dentro da função o x vira uma variavel local, fora da função ela é global e pode ser usada em qualquer lugar dentro do codigo.
myfunc()

print("Você é " + x )
print(z)
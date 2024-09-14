class Pessoa:#nomes de classes por padrão começa com as iniciais maiusculas.
    def __init__(self, nome, idade, cpf, etinia, nacionalidade):# i __init__ é uma função de inicialização, qual a classe vai iniciar primeiro e self serve para fazer uma caracteristica do objeto ou a caracteristica dele.
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.etinia = etinia
        self.nacionalidade = nacionalidade
        
    def dormir (sono):
        sono = input('A pessoa em questão esta com sono ? ')
        if sono == 'sim':
            print(f'Esta pessoa esta com sono, precisa dormir')
        else: 
            sono == 'não' 
            print('Esta pessoa não esta com sono')

pessoa1 = Pessoa('Luan', 25, '48403233809', 'branco', 'Brasileiro')
pessoa1.dormir()
Pessoa2 = Pessoa('Bartolomeu', 53, '48434645947', 'pardo', 'Brasileiro')


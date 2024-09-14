class Pessoa:
    # A classe Pessoa representa uma pessoa com atributos básicos.
    def __init__(self, nome, idade, cpf, etnia, nacionalidade):
        # O método __init__ inicializa os atributos da pessoa.
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.etnia = etnia
        self.nacionalidade = nacionalidade
        #self refere-se à instância atual da classe e é usado para acessar variáveis que pertencem à classe.
        
    def dormir(self):
        sono = input(f'{self.nome}, você está com sono? (responda com "sim" ou "não"): ').lower()
        if sono in ['sim', 's']:
            print(f'{self.nome} está com sono, precisa dormir.')
        elif sono in ['não', 'n', 'nao']:
            print(f'{self.nome} não está com sono.')
        else:
            print('Por favor, responda apenas com "sim" ou "não".')

# Criação de instâncias da classe Pessoa
pessoa1 = Pessoa('Luan', 25, '48403233809', 'branco', 'Brasileiro')
pessoa1.dormir()

pessoa2 = Pessoa('Bartolomeu', 53, '48434645947', 'pardo', 'Brasileiro')
pessoa2.dormir()
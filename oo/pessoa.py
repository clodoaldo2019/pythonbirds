class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)  # Note que passamos filhos como parâmetro da agora lista self.filhos

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3

    '''
    É possível sobrescrever o valor do atributo de uma classe. É só criar uma variável com o
     mesmo nome da classe pai. Na classe mutante a variável olhos tem o mesmo nome do atributo 
     olhos da classe Pessoa(). Assim, Mutante e os objetos derivados dela (a classe) passarão 
     a ter o número de olhos sobrescrito aqui.
    '''


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')     # renzo foi passado como filho de luciano
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome, 'é filho de luciano')
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(renzo.__dict__)
    print(luciano.__dict__)
    print('No de olhos Pessoa: ', Pessoa.olhos)
    print('No de olhos luciano: ', luciano.olhos)
    print('No de olhos renzo: ', renzo.olhos)

    '''
    Note que o valor do atributo olhos  vem do atributo de classe (variável de classe)
    olhos. Esse valor não está informado no __init__ e em nenhum método de classe da classe Pessoa.

    '''

    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_statico(), luciano.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonima')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(renzo, Pessoa))
    print(isinstance(pessoa, Homem))

    '''
    Ao referenciar renzo.olhos, primeiro o Python vai verificar se não foi atribuido algum valor a renzo.ollhos
    nas linhas executadas ateniormente (tipo: rezon.olhos=3). Em sequida vai verificar se foi atribuido algum 
    valor no momento da criação do objeto ( tipo: clodoaldo=Pessoa(olhos=5) ). Depois vai buscar no __dict__ do objeto renzo. 
    Se não achar, o Python vai tentar encontrar o atributo na classe a qual renzo pertence. Como a classe Homem 
    também não possui o atributo olhos, o Python vai tentar encontrar na classe pai da classe Homem 
    (que vai ser Pessoa). Finalmente, ele ainda vai buscar no atributo de classe (variável de classe).
     
    '''




import abc

#Criacao da classe pessoa
class Pessoa(abc.ABC):
    #Criacao do construtor
    def __init__(self , nome):
        self.__nome = nome
    #criacao do destrutor
    def __del__(self):
        pass
    
    #Criacao do Get
    #@property
    def getnome(self):
        return self.__nome
    
    @abc.abstractmethod

    def defenir_id(self):
        pass
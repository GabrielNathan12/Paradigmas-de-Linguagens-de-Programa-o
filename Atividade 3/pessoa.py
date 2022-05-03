import abc

#Classe de Pessoa
class Pessoa(abc.ABC):
    #Construtor
    def __init__(self , nome):
        self.__nome = nome
    #Destrutor
    def __del__(self):
        pass
    
    #Get
    #@property
    def getnome(self):
        return self.__nome
    
    @abc.abstractmethod
    def definir_id(self):
        pass
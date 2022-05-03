
#Classe do medicamento
class Medicamento():
    #Construtor
    def __init__(self , nome):
        self.__nome = nome
    
    #Destrutor
    def __del__(self):
        pass
    
    #Get
    #@property
    def nome_medicamento(self):
        return self.__nome
from pessoa import Pessoa

#Classe Medico
class Medico(Pessoa):
    #Construtor
    def __init__(self , nome):
        super().__init__(nome)
    
    #Destrutor
    def __del__(self):
        pass
    
    #Get
    #@property
    def nome_medico(self):
        return super().getnome()
    
    #Set
    def definir_id(self , identicacao):
        if(len(identicacao) > 3 ):
            print ("Erro , informe uma nova identicacao que nao seja maior que 3")
        else:
            self.identicacao = identicacao
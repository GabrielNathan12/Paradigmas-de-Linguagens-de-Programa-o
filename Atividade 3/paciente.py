from pessoa import Pessoa

#Classe Peciente
class Paciente(Pessoa):
    contPaciente = 0
    #Construtor
    def __init__(self , nome):
        super().__init__(nome)
        Paciente.contPaciente += 1
    
    #Desttrutor
    def __del__(self):
        Paciente.contPaciente -= 1

    @classmethod
    def pacientes_ativos(self):
        return Paciente.contPaciente
    
    #Set
    def definir_id(self , identificacao):
        if(len(identificacao) > 5):
            print ("Erro , informe um novo valor que nao seja maior que 5")
        
        else:
            self.identificacao = identificacao
    
    def definir_prontuario(self , prontuario):
        self.prontuario = prontuario
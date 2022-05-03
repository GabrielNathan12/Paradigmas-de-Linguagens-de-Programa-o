from medico import Medico

#Classe Prontuario
class Prontuario():
    #Construtor
    def __init__(self):
        self.__lista = []
    
    #Destrutor
    def __del__(self):
        pass
    
    #Get
    #@property
    
    def exibe_prontuario(self):
        self.exibe = ' '
        for x in self.__lista:
            self.exibe = self.exibe + '{} - {} - {} - {} - {}' .format(x['medicamento'] ,x['posologia'] , x['medico'] , x ['data'] , x['hora'])
            self.exibe = self.exibe + '\n'
        return print(self.exibe)

    #set
    #@???.setter
    def insere_procedimento(self , medicamento , posologia , medico , data , hora):
        NomeMedico = medico.nome_medico()
        NomeMedicamento = medicamento.nome_medicamento()
        __dicionario = {'medicamento' : NomeMedicamento , 'posologia' : posologia , 'medico' : NomeMedico , 'data' : data , 'hora' : hora}    
        self.__lista.append(__dicionario)
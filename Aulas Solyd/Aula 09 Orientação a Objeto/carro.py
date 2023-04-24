from veiculo import Veiculo
#Aqui estou criando uma sub-classe chamada carro que pega as caracteristicas do Veiculo como herança
# Alem das caracteristicas pega tbm os metodos nos quais sao sub-escritos caso voce deseje mudar alguma coisa
# ou apenas para mudar o tratamento
   
class Carro(Veiculo): #Um carro sempre sera um veiculo.

    def __init__(self, cor,marca,tanque):#o veiculo sera criado com esses argumentos 
#Nesse ponto digo que todo carro tera 4 rodas,         
        Veiculo.__init__(self, cor,4,marca,tanque)

# na class(Veiculo) nao existe um limite de combustivel portanto apenas carros terao seu metodo alterado  
    def abastecer(self, litros): 
        if self.tanque += litros > 50:#capacidade que o tanque tera 
            print('Erro tanque com capacidade inferior')
        else:
            self.tanque += litros
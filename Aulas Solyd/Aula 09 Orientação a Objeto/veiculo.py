class Veiculo:
                #Self (eu mesmo) o proprio objeto em questão

    def __init__(self, cor,rodas,marca,tanque):#caracteriscas que definem um veiculo, para ser construido
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        
    def abastecer(self, litros):#metodos que só um veiuclo pode fazer
        self.tanque += litros   #vai pegar a quantidade de litros e somar com o tanque

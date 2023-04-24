class Conta:

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        return

    def sacar(self, retirada):
        self.saldo -= retirada
        return
    
    def ver_saldo(self):
        print(self.saldo)

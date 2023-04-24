'''Crie um programa de gerenciamento bancario 
    programa podera criar clientes(nome, cpf, idade)
    e criar contas(cliente, saldo, limite) com metodos(sacar,depositar,ver saldo)
'''
from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Joao',27,'45970011824')
conta_Joao = Conta(cliente1, 100)

conta_Joao.sacar(20)
conta_Joao.ver_saldo()
conta_Joao.depositar(10)
conta_Joao.ver_saldo()

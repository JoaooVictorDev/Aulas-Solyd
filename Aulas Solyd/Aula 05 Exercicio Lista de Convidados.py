'''EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista'''


print('Programa Lista de Pessoas Python 1.0 ')
print('#####################################')

numero_convidado = int(input('Escreva o numero de convidados: '))

i=1
lista_convidado = []
escolha = 0

while i <= numero_convidado:
 convidado_novo = input('Nome do convidado #'+ str(i) + ': ')
 lista_convidado.append(convidado_novo)

 i += 1
   
print('Serão', numero_convidado , ' convidados')
print('\nLISTA DE CONVIDADOS')

for convidado_novo in lista_convidado:
    print(convidado_novo)

print("\nAdicionar mais pessoas? ")

escolha = 0

escolha = int(input('1.Sim      2.Não :'))

while escolha == 1:
    numero_convidado_mais = int(input('Escreva o numero de convidados a mais : '))
    numero_convidado = numero_convidado + numero_convidado_mais

    while i <= numero_convidado:
        convidado_novo = input('Nome do convidado #'+ str(i) + ': ')
        lista_convidado.append(convidado_novo)
        i += 1
        escolha -= 1

print('Serão', numero_convidado , ' convidados')
print('\nLISTA DE CONVIDADOS')

for convidado_novo in lista_convidado:
    print(convidado_novo)



    









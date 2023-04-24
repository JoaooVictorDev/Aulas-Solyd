'''Escreva uma funcao que recebe um objeto de uma coleção
e retorna o valor do maior numero dentro dessa coleção
faça outra funcao que retorna o menor numero '''

print('PROGRAMA COMPARADOR DE NUMEROS DE UMA LISTA 1.0')
print('###############################################')
print('\n')

print('Digite 5 numeros para serem verificados: ')


def maior(lista): #lista é somente um exemplo quando for usar a funcao use com o valor desejado 
    maior_item = lista[0]
    for i in lista:
        if i > maior_item:              #nessa lista nao existe dados somente demonstração
            maior_item = i 
    return maior_item

def menor(lista): #lista é somente um exemplo quando for usar a funcao use com o valor desejado 
    menor_item = lista[0]
    for i in lista:
        if i < menor_item:              #nessa lista nao existe dados somente demonstração
            menor_item = i 
    return menor_item

lista_numero = []      #criação da lista vazia

while len(lista_numero) < 5:
    numero_novo = input('__: ')
    lista_numero.append(numero_novo)                        #colocando novos nomes na lista
    if len(lista_numero) == 5:
        print('pronto')                               #funcao é parecido com uma formula matematica que voce mesmo cria
        break

print(maior(lista_numero), 'Esse é o maior numero da lista')  #usando a funcao na lista_numero 
print(menor(lista_numero), 'Esse é o menor numero da lista')


  
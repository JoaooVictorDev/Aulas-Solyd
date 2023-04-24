
#TIPOS DE COLEÇÕES


minha_lista = ['maria', 'joao'] #dinamico segue uma ordem e pode ser alterada a quantidade e os itens   LIST list
minha_tupla = ('carlos','vinicius')  #nao é dinamico voce nao pode alterar a quantidade de itens nem add nem removendo   TUPLA tuple
meu_dicionario = {'nome' : 'diego','idade' : 48} #DICIONARIO NOME = KEY   DIEGO = VALUE
meu_conjunto = {'jose', 'davi'} #VOCE NAO PODE ADICIONAR ITENS IGUAIS DENTRO DE UM CONJUNTO, NAO É ORDENADO VOCE NAO PODE PEGAR O NUMERO (1)

#na TUPLA existe indice entao voce pode acessar o arquivo 0, 1, 2, 3 ...
#o FOR pode ser usado para todas as coleçoes 

for i in meu_conjunto: 
    print(i)

#voce pode perguntar se determinado item esta dentro de uma coleção

if 'carlos' in minha_tupla:
    print('carlos está dentro da tupla')

print(meu_dicionario['idade'])

 #em qualquer coleção voce pode usar o len para contar quantas coisas tem dentro dessa coleção
print(len(minha_lista))

#para valores dentro de meu_dicionario imprima o valor
for valor in meu_dicionario.values():
    print(valor)

#para chave(key) dentro de meu_dicionario imprima o chave(key)
for keys in meu_dicionario.keys():
    print(keys)

#mudando o value de uma chave no dicionario
meu_dicionario['nome'] = 'fabricio'
print(meu_dicionario)

#para criar um nome elemento dentro do dicionario, para apagar  usar CLEAR
meu_dicionario['endereço'] = 'rua das gaivotas'
meu_dicionario['telefone'] = '45999871264'
meu_dicionario.clear

#para adicionar algo dentro de um conjunto
meu_conjunto.add('joaquim')

#diferenças de usar uma lista e um conjunto
'''No conjunto nao existe um indice entao os itens nao seguem uma ordem numerica 0,1,2,3,4,5,6...
   Na lista eles já são ordenados começando no 0...2 
   Quando voce manda um programa fazer uma busca dentro de uma lista'''

minha_lista = ['Maria' , 'Joao' , 'Guilherme']
meu_conjunto = ['Maria' , 'Joao' , 'Guilherme']

if 'Maria' in meu_conjunto:
    print('Maria esta no conjunto')       #encontra o item com maior velocidade pois vai direto nele

if 'Maria' in minha_lista:                #numa pesquisa dentro da lista se passa por cada item verificando se aquele item nao é o pesquisado
    print('Maria esta na lista')

#Simbologia das coleções
LISTA = []
TUPLA = ()
DICIONARIO = {}
CONJUNTO = set()
   



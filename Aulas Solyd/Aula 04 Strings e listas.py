frase = 'Ola, Mundo' #dentro de um argumento cada caractere conta conta como um numero espaços virgulas começando sempre pelo zero
lista_nomes = ['joao','maria','paula','joao','joao','joao'] #dentro de uma lista com conchetes[] cada item é um numero começando por zero

frase  #frase é uma string que é composta por frases, ou varios caracteres
lista_nomes  #lista_nomes é uma list composta por varios elementos


print (lista_nomes[0]) #aqui vc seleciona um para exibir
print(frase[3:4:2])#aqui voce seleciona de qual item começa a impressão e qual termina
                   #o numero 2 é a quantidade de passos que ele pulara de item ou caractere o padrao é um
print(lista_nomes[-1])#para imprimir o ultimo item de uma lista
print(frase[::-1])#para imprimir uma sequencia de tras para frente

lista_nomes.append('diego')#para adicionar um item/nome na lista sempre no final 
print(lista_nomes)

lista_nomes.remove('maria')#para remover um nome da lista
print(lista_nomes)

lista_nomes.clear#limpa a lista 
print(lista_nomes)

lista_nomes.insert(2,'kaique')#numero da posicao que o nome sera incerido 
print(lista_nomes)

lista_nomes[0] = 'mathueus'#para mudar o nome de algum item da lista
print(lista_nomes)

contador_joao = lista_nomes.count('joao')#contador_joao variavel que sempre executara essa ação  #para contar quantos nomes iguais existem na lista
print(contador_joao)

print(len(frase))#para contar quantos itens existem dentro 

print(lista_nomes.pop())#imprimi ultimo valor da lista e o remove da lista
print(lista_nomes.pop())
print(lista_nomes)

print(frase.lower())#durante esse print a frase fica toda em minuscula
print(frase.upper)#durante esse print a frase fica toda em maiuscula

frase_separada = frase.split(',')#transforma uma string em uma list separando a no caractere desejado
print(frase_separada)

frase_nova = frase + "Como vai voce?"
print(frase_nova)
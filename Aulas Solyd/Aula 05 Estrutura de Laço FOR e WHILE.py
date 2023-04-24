nomes = ['joao', 'maria', 'baki', 'itachi']

palavara = "palavra"

for letra in palavara:
    print(letra)

for letra in range(len(palavara)):
    print(letra)

print('______________________________________')

lista_numeros = range(5) #cria cinco numeros comecando do 0 .. 4
                        #range(5, 10, 2) primeira casa onde inicia a contagem, segunda até onde é pra contar, terceira a quantidade que se pula de um numero ao outro

for item in lista_numeros: #PARA(for) cada item DENTRO(in) lista_numeros: imprima item 
    print(item)



print('______________________________________')

for nome in nomes:        #for para cada item dentro dessa coleção execute a ação até que tenho
 print(nome)                                #sido executado com todos os itens de dentro da coleção
    

print('______________________________________')


for i in range(0,100,2):   # para cada tem dentro do range(vai começar no zero e ir até o 100 pulando duas casas)
    print(i)


print('______________________________________')
    

for it in range(len(nomes)):    #usando len voce faz com que cada item seja acessado
    print(nomes[it])
    nomes.append('pikachu')     #para cada item dentro da coleção adicione pikachu a coleção 

print(nomes)    

print('______________________________________')

a = 0 

while a < 10:                                   #laço de repeticao WHILE assim como IF só executa a ação se o valor for TRUE 
    print('A nao é maior que 10: ', a)          #voltando sempre para o inicio e fazendo a comparação ate aparecer FALSE
    a= a+1
 
print('A é maior que 10: ', 10)    

print('______________________________________')


'''b = 0 
while True
print('Loop infinito', b)                       loop infinito programa nunca vai parar até a memoria do computador acabar
b = b + 1

while b < 10:
    print('Loop infinito', b)                   cuidado para coisas assim nao aconteceram já que esse valor nao esta sendo alterado
                                                sempre ficara printando '''

print('soma')

c = 0
c= c + 1
c += 1                #maneira simplificada de escrever
print(c)


print('______________________________________')



lista_frutas = ['maca','pera','abacaxi','melancia','goiaba']
contador = 0

for fruta in lista_frutas:                               #para contar quantas coisas dentro da lista_frutas
    contador += 1

print(contador) 

print(len(lista_frutas))                                 #usando o comando lens é mais facil

numero = 0
while True:                                           #loop infinito porem pode ser parado usando BREAK 
    print(numero)
    if numero == 20:
        break
    numero += 1

print('saiu do while')
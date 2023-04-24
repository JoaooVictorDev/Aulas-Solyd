#FUNÇÕES

#Metodo é uma funcao sem 'return'

#Uma funcao é usada para ações que sempre vao se repetir dentro do programa, como por exemplo a soma de numeros numa calculadora

def soma(number1,number2):  #def é a funcao quer dizer que toda vez que 'soma' for chamada sera esse conjunto de acoes que serao utilizadas
    resposta = number1 + number2 #soma = armazenar numeros na variavel soma               #reposta = adicao dos numero 1 e numero2
    return resposta            # return aqui voce coloca a variavel que aparecera quando pedirem pela funcao

retorno = soma(4,5)           #como chamar uma funcao
print(retorno)

print('_________________________________')

def sete_item(i):     #funcao que conta quantos coisas existem na função    
    if len(i) == 7:   #conta quantas itens existe dentro d i se tiver 7 return True senao return False
        return True
    else:
        return False
                                   #ate esse ponto nao tinha sido atribuido valor a i
print(sete_item('1234567'))   #estou atribuindo a string '1234567' a i

if sete_item('1234567'): #se sete_item('1234567') for verdadeiro ira executar
    print('realmente tem 7 itens')
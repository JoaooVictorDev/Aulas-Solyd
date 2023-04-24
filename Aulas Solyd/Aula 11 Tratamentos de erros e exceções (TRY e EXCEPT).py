import time

try:#usa a para iniciar a tentativa de uma acao se nao for possivel realizar ett execute a except
    a = 2/ 0#aqui daria um erro
except:#a execao 
    print('Aconteceu um Erro')

try:
    a = 2/0
except ZeroDivisionError:#voce pode especificar o tipo de erro que essa except ira tratar
        print('Zero nao é divisivel ')
 
 try:
    afdsgdsg()
 # as err coloca o valor da except dentro da variavel err, para que possa ser printado o err que aconteceu
except Exception as err:#Execption= ira tratar todas as except
        print('Aconteceu alguma coisa de errado: ',err)
 

 #Tratar os erros bens pode fazer seu programa rodar muito melhor


 #try e except só exsitem em liguagens de alto nivel

 

nome = 'joao' #se estiver entre aspas será considerado str, string, texto
idade = 21     #numero inteiro
altura = 1.83   #numero decimal sempre usando o ponto quando a casa decimal começar no 1.500 nao precisa por
tipo_altura = type(altura)
tipo_idade = type(idade)
tipo_nome = type(nome)

pet = input('qual bicho voce tem de estimação ?') #input para inserir um argumento(entrada de dados), sempre me retornara um objeto do tipo str

print(nome) #print para exibir (saida de dados)
print(tipo_nome)
print(idade)
print(tipo_idade)
print(altura)
print(tipo_altura)

print(nome, 'tem isso de altura',altura, 'e', idade,'anos' ) 
#PARA SEPARAR AS VARIAVEIS PODE SE USAR ,(DA ESPAÇO ENTRE OS VALORES) OU + (NAO DARA ESPAÇO ENTRE OS VALORES, POREM TODOS PRECISAM SER DO TIPO STR)

print(nome + ' tem isso de altura ' + str(altura) + 'e' + str(idade) + 'anos' ) 
#QUANDO TODOS OS VALORES SÃO STR UTILIZE UM 'ESPAÇO' NO FINAL OU COMEÇO DA FRASE PARA DAR ESPAÇO

print(nome, 'tem isso de altura' ,altura, 'e', idade,'anos e um', pet, 'de estimação')


print("Escolha seu pokemon \n 1 - Chamander \n 2 - Squirtle \n 3 - Bulbasaur")

escolha = input("Qual voce escolhe?")

''' "if" faz a primeria pergunta se a reposta for "True" finaliza o programa
    "elif" ou else if faz a pergunta caso o primeiro if tenha sido "False" 
    "else" se if for "False" para de fazer comparações e finaliza o programa
'''
if escolha == "1":
    print("Voce escolheu Chamander")
elif escolha == "2":
    print ("Voce escolheu Squirtle")
elif escolha == "3":
    print("Voce escolheu Bulbasaur")
else:
    print("Voce errou")




var_falso = False
var_vdd = True #variavel do tipo booleano ou boolean 

#para fazer uma comparação podemos usar: maior ou igual >=; menor ou igual <=; igual ==; diferente !=; maior >; menor <;  

if var_vdd == True:   # "if" comando para comparar se
    print("Acertou") #esse comando só acontecera quando a pergunta de cima for respondida com "True"
else:                 # caso o resultado do "if" seja falso acontecera ele (senao)
    print("Errou")    

1==1 and 1==2 #quando se usa o "and" vc precisa que os dois requisitos sejam "True" para que ele aconteça
1==1 or 1==2  #quano se usa o "or" vc precisa que apenas um dos dois seja "True" para que aconteça

if not True: #NOT faz com que todo valor True vire False, e todo valor False vire True
    print("Entrou no if")
else: 
    print("entrou no else")
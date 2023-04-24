'''pergunte idade peso e altura
    decidir se esta apta a servir o exercito
    (condicoes para servir maior de 18 pelo menos 60 kg pelo menos 1,70 metros )'''

print("Bem vindo ao alistamento militar python")
nome = input("Qual seu nome?")
idade = int(input("Quantos anos voce tem?")) #colocar um conversor atras do input caso precise que a variavel seja diferente de str
peso = float(input("Quanto voce pesa?"))
altura = float(input("Qual sua altura?"))



if idade >= 18 and peso >= 60 and altura >= 1.70:
    print("Parabens", nome, "voce atende os requisitos para servir o exercito")
else:
    print(nome,"lamentamos mas voce nao atende os requisitos")
import sys

argumentos = sys.argv #cria uma lista usando cada palavra digitada no terminal separada por espaço

def soma(n1 , n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]) , float(argumentos[3]))

elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]) , float(argumentos[3]))

print(resp)

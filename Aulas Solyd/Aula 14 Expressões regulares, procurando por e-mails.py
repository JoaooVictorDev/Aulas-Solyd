import re 
import requests

#regex101.com  site para testar suas expressoes


requisicao = requests.get('https://loucosporcoxinha.com.br')#Acessando o site no qual será pego o e-mail

#findall pesquisa por todas as palavras dentro do objeto que coencidem com a expressao regular desejada
#o r antes da expressao é para cancelar funçoes de caracteres
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)#passando onde deve ser verificado se existe a expressao

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')


string = 'o gato de botas casou com a gata sem garras'
# search procura pela primeira palavra que cumprir os requisitos da expressao
pesquisa = re.search(r'gat\w', string)

if pesquisa:
    print(pesquisa)
else:
    print('Padrão não encontrado')


(?<=)#Com esse comando voce determina pelo oq deve ser procurado
(?=)#onde deve terminar a procura

#Exemplo

carro = re.findall(r'(?<=botas)\w+(?=com)', string)
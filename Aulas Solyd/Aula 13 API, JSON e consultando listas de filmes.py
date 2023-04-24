'''API um banco de dados que qualquer um pode acessar atraves da internet
os sites são estruturados geralmente em javascript por isso a biblioteca json
para transformar akelas informações em objetos python.'''
import requests
import json

req = None

def requisicao(titulo):#A função pega o nome do titulo e coloca junto da URL
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=aa259fba&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except Exception:
        print("Erro de Conexão")
        return None

def printar_detalhes(filme):#Informações contidas dentro do dicionario  
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])

sair = False
while not sair: #Loop para perguntar ao usuario qual filme pesquisar
    op = input('Escreva o titulo do filme ou SAIR para fechar: ')
    if op == 'SAIR':
        print('Até a proxima...')
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
            print()#Print vazio para dar um espaço entre as execuções do programa
        else:
            printar_detalhes(filme)
            print()

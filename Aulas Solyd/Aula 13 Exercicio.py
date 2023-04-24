import requests
import json

req = None 

def filme_lista(titulo):
    lista = []
    for i in range(1,101):#NUMERO DE PAGINAS QUE O PROGRAMA DEVE PERCORRER
        try:
            print('Pesquisando na pagina', i)#MOSTRA POR QUAIS PAGINAS ELE ESTA PERCORRENDO
            req = requests.get('http://www.omdbapi.com/?apikey=aa259fba&s='+ titulo + '&type=movie&page='+str(i))#ENTRANDO NO SITE 
            dicionario = json.loads(req.text)#TRANSFORMANDO O TEXTO DO SITE(JSON) EM UMA VARIAVEL
            if dicionario['Response'] == 'False':#SE A RESPOSTA FOR FALSE PARA O PROGRAMA
                break
            else:
                for filme in dicionario['Search']:
                    titulo_filme = filme['Title']
                    ano_filme = filme['Year']
                    nome_na_lista = titulo_filme + ' (' + ano_filme + ')'#CRIANDO O NOME QUE SERA USADO NA LISTA COM AS INFORMAÇÕES DO DICIONARIO
                    lista.append(nome_na_lista)#ADICIONANDO O FILME A LISTA DE FILME
        
        except Exception:#SE ACONTECER QUALQUER ERRO O PROGRAMA PARA
            print('Erro de Conexão')
    return lista 
#INICIO DO PROGRAMA 
sair = False
while not sair:#LOOP PARA PERGUNTAR O QUE DEVE SER FEITO  
    nome_filme = input('Escreva o nome do filme ou SAIR para fechar o programa: ')
    if nome_filme == 'SAIR':#CASO A RESPOSTA SEJA 'SAIR' O PROGRAMA É ENCERRADO
        print('Obrigado por usar o programa...')
        sair = True
        exit()
    else:
        lista_de_filmes = filme_lista(nome_filme)
        print('Numero de resultados encontrados: ',len(lista_de_filmes))
        for filme in lista_de_filmes:#PARA PRINTAR O NOME DE CADA FILME EM UMA LINHA
            print(filme)

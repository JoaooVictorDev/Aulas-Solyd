import requests

requisicao = None
                        #Assim se cria uma requisição para o site
try:
    requisicao = requests.get("https://putsreq.com/LCVZKapP43cmbCqDUSSJ")
    print(requisicao.text)

except Exception as e :
    print("Requisicao deu erro", e)

'''_______________________________________'''


#Voce passa os que gostaria de mudar

cabecalho = {'User-agent': 'Windows 12',
              'Referer' : 'https://google.com'} #De onde voce esta vindo 

meus_cookies= {'Ultima-visita': "10-10-2020"}

dados = {'username': 'guigui',
        'password': 'gui123456'}
                        
try:        #enviando dados voce usa o post, get voce usa para acessar 
    requisicao = requests.post("https://putsreq.com/LCVZKapP43cmbCqDUSSJ", #Para mudar o paramentro de alguma parte voce passa o nome dele
                                headers= cabecalho
                                data= dados
                                cookies= meus_cookies)
    texto = requisicao.text

except Exception as e :
    print("Requisicao deu erro", e)

print(texto)
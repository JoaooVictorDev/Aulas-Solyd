import requests
import time
import datetime
import json


try:
    requisao = requests.get('http://api.promasters.net.com.br/cotacao/v1/valores')
    resposta = json.loads(requisao.text)
except Exception:
    print('erro de conexao')

print('_____COTAÇÃO_____', datetime.datetime.now())
print('Dólar:', resposta['valores']['USD']['valor'])
print('Euro:', resposta['valores']['EUR']['valor'])
print('BITCOIN:', resposta['valores']['BTC']['valor'])
time.sleep(20)
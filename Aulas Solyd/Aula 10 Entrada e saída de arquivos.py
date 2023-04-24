#Comando para abrir arquivos no computador se ele estiver na mesma pasta que o arquivo nao precisa
#especificar o caminho , ***USAR \\ BARRAS INVERTIDAS PARA DIZER O CAMINHO
open('arquivo.txt', 'r')


arquivo = open('arquivo.txt', 'w')
for i in range(1,1000):
    arquivo.write(str(i)+'\n')            #para escrever dentro do arquivo


print(arquivo.read()) #Para ler o que tem dentro do arquivo


#R read abrir o arquivo,             Se deixar o segundo argumento em branco, 'r' é sempre padrao
#W write  salvar o arquivo,
#R+ executa os dois comandos
#A append adiciona no final do arquivo
#B usar para todos os tipos de arquivos que nao sejam texto

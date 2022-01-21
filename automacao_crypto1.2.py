from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pywhatkit
import csv
import time

#LISTA DE DICIONARIOS COM OS PARAMETROS PARA COTAÇÕES
dict_cripto = [
    {'BCOIN':'bombcrypto'},
    {'CCAR':'cryptocars'},
    {'CMC':'cryptomotorcycle'},
    {'SLP':'smooth-love-potion'},
    {'CGAR':'cryptoguards'},
    {'BTC':'bitcoin'}
    ] 

# PEGANDO COTAÇÕES
nav = webdriver.Chrome()

def pegar_cotacao(moeda_nome, link):
    nav.get(f'https://coinmarketcap.com/pt-br/currencies/{str(link)}/')
    moeda = nav.find_element_by_xpath("""
        /html/body/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input
        """).get_attribute('value')
    return f'{moeda_nome}:\t{moeda}'

#VARIAVEL RESULTADO PARA ARMAZENAR A STR DAS COTACOES
resultado = 'Seguem cotações:'

#FOR EXECUTA A FUNCAO DIVERSAS VEZES PARA PEGAR CADA UMA DAS COTACOES
for i in dict_cripto:
    for m,u in i.items():
        resultado = resultado + f'\n' + pegar_cotacao(m,u)

nav.close()

#ENVIANDO COTAÇÕES VIA WHATSAPP
cel = csv.reader(open('cel.csv'), delimiter = ',')

print(resultado)

try:
    for num in cel:

        
        pywhatkit.sendwhatmsg_instantly(f'+5511{num}', resultado, tab_close = True,)
        print(f'Mensagem enviada para o número: {num} com sucesso!!')
        time.sleep(3)
    print('ENVIOS FINALIZADOS!')
except ValueError as v:
    print(f"ERRO - MENSAGEM NAO ENVIADA!ERRO: {v}") 
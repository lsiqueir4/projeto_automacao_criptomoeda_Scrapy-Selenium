from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pywhatkit
import csv
import time

nav = webdriver.Chrome()

# PEGANDO COTAÇÕES

def pegar_cotacao(nome_var, link):
    cotacao = str(nome_var)
    nav.get(f'https://coinmarketcap.com/pt-br/currencies/{link}/')
    cotacao = nav.find_element_by_xpath("""
        /html/body/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/input
        """).get_attribute('value')
    return cotacao

# BOMBCRYPTO
cotacao_bcoin = pegar_cotacao('cotacao_bcoin','bombcrypto')
# CRYPTOCARS
cotacao_ccar = pegar_cotacao('cotacao_ccar','cryptocars')
# CRYPTOMOTORCYCLE
cotacao_cmc = pegar_cotacao('cotacao_cmc','cryptomotorcycle')
# SMOOTHLOVEPOTION
cotacao_slp = pegar_cotacao('cotacao_slp','smooth-love-potion')
# CRYPTOGUARDS
cotacao_cgar = pegar_cotacao('cotacao_cgar','cryptoguards')

nav.close()

#IMPRIMINDO RESULTADO
resultado = f"\nBombCrypto(BCOIN):\t{cotacao_bcoin}\nCryptoCars(CCAR):\t{cotacao_ccar}\nCryptoMotorCycle(CMC):\t{cotacao_cmc}\nSmoothLovePotion(SLP):\t{cotacao_slp}\nCryptoGuards(CGAR):\t{cotacao_cgar}\n"
print(resultado)

#ENVIO MENSAGEM WHATSAPP
cel = csv.reader(open('cel.csv'), delimiter = ',')

try:
    for num in cel:
        pywhatkit.sendwhatmsg_instantly(f'+5511{num}', resultado, tab_close = True)
        print(f'Mensagem enviada para o número: {num} com sucesso!!')
        time.sleep(3)
    print('ENVIOS FINALIZADOS!')
except ValueError as v:
    print(f"ERRO - MENSAGEM NAO ENVIADA!ERRO: {v}") 

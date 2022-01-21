from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pywhatkit
import datetime
import time


nav = webdriver.Chrome()

# PEGANDO COTAÇÕES

# BOMBCRYPTO
nav.get('https://coinmarketcap.com/pt-br/currencies/bombcrypto/')
cotacao_bcoin = nav.find_element_by_xpath("""
    /html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/input
    """).get_attribute('value')

# CRYPTOCARS
nav.get('https://coinmarketcap.com/pt-br/currencies/cryptocars/')
cotacao_ccar = nav.find_element_by_xpath("""
    /html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/input
    """).get_attribute('value')

# CRYPTOMOTORCYCLE
nav.get('https://coinmarketcap.com/pt-br/currencies/cryptomotorcycle/')
cotacao_cmc = nav.find_element_by_xpath("""
    /html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/input
    """).get_attribute('value')

# SMOOTHLOVEPOTION
nav.get('https://coinmarketcap.com/pt-br/currencies/smooth-love-potion/')
cotacao_slp = nav.find_element_by_xpath("""
    /html/body/div/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/input
    """).get_attribute('value')

# CRYPTOGUARDS
nav.get('https://coinmarketcap.com/pt-br/currencies/cryptoguards/')
cotacao_cgar = nav.find_element_by_xpath("""
    /html/body/div/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/input
    """).get_attribute('value')

nav.close()

#PEGANDO HORA E MINUTO ATUAL


#IMPRIMINDO RESULTADO NO CONSOLE
resultado = f"\nBombCrypto(BCOIN):\t{cotacao_bcoin}\nCryptoCars(CCAR):\t{cotacao_ccar}\nCryptoMotorCycle(CMC):\t{cotacao_cmc}\nSmoothLovePotion(SLP):\t{cotacao_slp}\nCryptoGuards(CGAR):\t{cotacao_cgar}\n"
print(resultado)

#ENVIO MENSAGEM WHATSAPP
cel = ('948158251', '956663035', '969792493')

try:
    for num in cel:
        #now = datetime.datetime.now().time()
        #hora_atual = int(now.strftime('%H'))
        #minuto_atual = int(now.strftime('%M')) - o _instantly não precisa passar variavel de tempo, ele envia instantaneamente
        pywhatkit.sendwhatmsg_instantly(f'+5511{num}', resultado, tab_close = True)
        print(f'Mensagem enviada para o número: {num} com sucesso!!')
        time.sleep(3)
    print('ENVIOS FINALIZADOS!')
except ValueError as v:
    print(f"ERRO - MENSAGEM NAO ENVIADA!ERRO: {v}") 
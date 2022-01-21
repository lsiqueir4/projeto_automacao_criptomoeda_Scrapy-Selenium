from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 



nav = webdriver.Chrome() #webdrive define o navegador que o script utilizará
nav.get('https://www.google.com/') #.get vai acessar o link informado
#encontrando elemento na pag, no caso o campo de busca
nav.find_element_by_xpath ("""
    /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input
    """).send_keys("cotação dolar", Keys.ENTER) #digita o texto e aperta enter
cotacao_dolar = nav.find_element_by_xpath("""
    /html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/div[2]/span[1]
    """).get_attribute('data-value')

nav.get('https://www.google.com/') #.get vai acessar o link informado
#encontrando elemento na pag, no caso o campo de busca
nav.find_element_by_xpath ("""
    /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input
    """).send_keys("cotação euro", Keys.ENTER) #digita o texto e aperta enter
cotacao_euro = nav.find_element_by_xpath("""
    /html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/div[2]/span[1]
    """).get_attribute('data-value')

print(f'Dolar: {cotacao_dolar} | Euro: {cotacao_euro}')
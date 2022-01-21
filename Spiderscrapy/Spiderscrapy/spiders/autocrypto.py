import os, time, json
from autocryptospider import Autocryptospider

lista_dicionario = []

#EXECUTA SCRAPY
def auto_crypto(tempo=int):
    try:
        raw_string = r"scrapy runspider .\autocryptospider.py -o cotacao.json"
        os.system(raw_string)
        time.sleep(tempo)
        print('DADOS COLETADOS COM SUCESSO!')
    except:
        print('ERRO! WEB SCRAP NÃO EFETUADO!')

#PEGAR ARQUIVO JSON GERADO E ARMAZENA NA VARIAVEL LISTA_DICIONARIOS
def pegar_json():
    try:
        with open ('cotacao.json') as json_file:
            cotacoes = json.load(json_file)
        time.sleep(4)
        for cotacao in cotacoes:
            lista_dicionario.append(cotacao)
        print('JSON COLETADO COM SUCESSO!')
        #EXCLUINDO JSON
        try:
            os.remove('cotacao.json')
            print('JSON EXCLUIDO COM SUCESSO!')
        except:
            print('NÃO FOI POSSIVEL EXCLUIR O JSON')
    except ValueError as v:
        print(f"ERRO! COLETA DO ARQUIVO JSON FALHOU, ERRO:{v}")

#FORMATANDO AS COTAÇÕES PARA FORMATO DE TEXTO(PARA ENVIAR POR EMAIL, WPP ETC)
def formatar_cotacao():
    horario_atual = time.ctime()
    resultado_final = f'[{horario_atual}] Cotações:'
    for dicionario in lista_dicionario:
        resultado_final  += f"\n {dicionario['nome']}({dicionario['sigla']}) = {dicionario['cotacao']}"
    return resultado_final
  
auto_crypto(4)
pegar_json()
print(formatar_cotacao())
import os, time, json, pywhatkit, csv

lista_dicionario = []

horario_atual = time.ctime()

#EXECUTA SCRAPY
def auto_crypto():
    try:
        raw_string = r"scrapy runspider .\autocryptospider.py -o cotacao.json"
        os.system(raw_string)
        time.sleep(3)
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
    resultado_final = f"[{horario_atual}] Cotações:"
    for dicionario in lista_dicionario:
        resultado_final += f"\n {dicionario['nome']}({dicionario['sigla']}) = {dicionario['cotacao']}"
    time.sleep(2)
    return resultado_final
    

cel = csv.reader(open('cel.csv'), delimiter = ',')

def enviar_whats():
    
    try:
        for num in cel:
            pywhatkit.sendwhatmsg_instantly(f'+5511{num}', formatar_cotacao(), tab_close = True,)
            print(f'Mensagem enviada para o número: {num} com sucesso!!')
            time.sleep(3)
        print('ENVIOS FINALIZADOS!')
    except ValueError as v:
        print(f"ERRO - MENSAGEM NAO ENVIADA!ERRO: {v}") 
  
auto_crypto()
pegar_json()
enviar_whats()
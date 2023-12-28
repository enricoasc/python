import os
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from zipfile import ZipFile

def salvaLog(err):
    print("OS error:", err)
    # Informa no Log
    data_public = datetime.datetime.now()
    data_public_str = data_public.strftime('%d/%m/%Y %H:%M')
    f = open("log.txt", "a")
    f.write(f'\n[{data_public_str} (BLC001)] {err.msg} \n')
    f.close()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def startTradeMasterArq() :
    while True:
        try:
            # :: BLC001 - bloco de codigo acessa trade master
            # ===============================================

            os.system("cls")
            print('# :: 1.2 baixa o ultimo dirver do chrome')
            print('# ============================================')
            print('# ')

            servico = Service(ChromeDriverManager().install())
            navegador = webdriver.Chrome(service=servico)
            time.sleep(4)

            os.system("cls")
            print('# :: 1.3 acessa a pagina e faz login')
            print('# ============================================')
            print('# ')
            navegador.get('https://portal.trademaster.com.br/login')
            navegador.find_element('xpath','//*[@id="email"]').send_keys('trademaster.auto@riobrancopetroleo.com.br')
            time.sleep(1)
            navegador.find_element('xpath','//*[@id="password"]').send_keys('1!2Y5PV8qc')
            time.sleep(1)
            navegador.find_element('xpath','//*[@id="root"]/main/div[2]/div/div[1]/div/form/button').click()
            time.sleep(8)

            os.system('cls')
            print('# :: 1.4 seleciona a opção de limites e clica para baixar a planilha no email')
            print('# ============================================')
            print('# ')
            navegador.find_element('xpath','//*[@id="navbar_container"]/nav/ul/li[5]/a/span/span[2]/i').click()
            time.sleep(4)
            navegador.find_element('xpath','//*[@id="navbar_container"]/nav/ul/li[5]/ul/li/a/span').click()
            time.sleep(10)
            navegador.find_element('xpath','//*[@id="root"]/div/div/main/div[2]/div/div[1]/div/button/span').click()
            time.sleep(4)

            os.system('cls')
            print('# :: 1.5 fecha o navegador')
            print('# ============================================')
            print('#')
            navegador.close()
            time.sleep(30)

        except OSError as err:
            salvaLog(err)
            break

        except Exception as err:
            salvaLog(err)
            break

        try:
            # :: BLC002 - bloco que acessa o email e baixa anexo
            # ==================================================
            os.system('cls')
            print('# :: 1.6 acessa o email e baixa a planilha de limites')
            print('# ============================================')
            print('# ')
            navegador = webdriver.Chrome(service=servico)
            navegador.get('https://outlook.office.com/mail/')

            os.system('cls')
            print('# :: 1.7 loga no email :')
            print('# ============================================')
            print('#')
            time.sleep(2)
            navegador.find_element('xpath','//*[@id="i0116"]').send_keys('trademaster.auto@riobrancopetroleo.com.br')
            navegador.find_element('xpath','//*[@id="idSIButton9"]').click()

            time.sleep(2)
            navegador.find_element('xpath','//*[@id="i0118"]').send_keys('drbp@2023Petro')
            time.sleep(2)
            navegador.find_element('xpath','//*[@id="idSIButton9"]').click()
            time.sleep(3)
            navegador.find_element('xpath','//*[@id="idBtn_Back"]').click()

            os.system('cls')
            print('# :: 1.8 baixa o arquivo limits.zip')
            print('# ============================================')
            print('#')
            time.sleep(5)
            navegador.find_element('xpath','//*[@title="contato@trademaster.com.br"]').click()
            time.sleep(5)
            navegador.find_element('xpath','//*[@title="limites.zip"]').click()

            os.system('cls')
            print('# :: 1.9 deleta o email')
            print('# ============================================')
            print('#')
            navegador.find_element('xpath','//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[3]/div/span/button[1]').click()
            time.sleep(3)

            os.system('cls')
            print('# :: 1.10 fechar nvegador')
            print('# ============================================')
            print('# ')
            navegador.close()

        except Exception as err:
            salvaLog(err)
            break

        try:
            # :: BLC003 - extrai o arquivo e deleta o original
            # ==================================================

            os.system('cls')
            print('# :: 1.11 extrair os arquivos')
            print('# ============================================')
            print('# ')
            z = ZipFile('C:\\Users\\Administrator\\Downloads\\limites.zip')
            time.sleep(3)
            z.extractall()
            time.sleep(3)
            z.close()
            time.sleep(3)

            os.system('cls')
            print('# :: 1.12 deleta zip')
            print('# ============================================')
            print('# ')
            os.remove('C:\\Users\\Administrator\\Downloads\\limites.zip')

        except Exception as err:
            salvaLog(err)
            break
        break
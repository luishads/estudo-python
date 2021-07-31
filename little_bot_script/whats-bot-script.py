# ->Antes de tudo, no Terminal execute os comandos 'pip install selenium' e depois 'pip install webdriver_manager'

#Esse envia apenas uma msg de texto simples
#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#navegar até o whats web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') 
time.sleep(15)
#definir contatos 
contatos = ['Um contato', 'Um grupo', 'Outro contato']
mensagem = 'isso é uma msg teste'
#buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click() 
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
#Enviando mensagem
def enviar_mensagem(mensagem):
    campo_msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_msg[1].click
    time.sleep(3)
    campo_msg[1].send_keys(mensagem)
    campo_msg[1].send_keys(Keys.ENTER)
#loop para enviar para todos os contatos
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# ->Antes de tudo, no Terminal execute os comandos 'pip install selenium' e depois 'pip install webdriver_manager'

#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegar até o whats web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
driver.maximize_window() 
time.sleep(15)

#definir contatos 
contatos = ['Um contato', 'Um grupo', 'Outro contato']  #Lista de contatos aos quais a msg serão enviadas

#definir msg
mensagem = 'mensagem exemplo'   #Msg de texto a ser enviada

#buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click() 
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Enviando mensagem com foto
def enviar_mensagem(mensagem):
#Escrevendo mensagem
    campo_msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_msg[1].click()
    time.sleep(2)
    campo_msg[1].send_keys(mensagem)
    time.sleep(2)

#Anexando imagem
    campo_anx = driver.find_element_by_xpath('//div[contains(@title,"Anexar")]')
    campo_anx.click()
    #achando foto no pc
    input_ing = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    input_ing.send_keys('Caminho\\Para\\imagem.jpg')  # <- coloque aqui o caminho onde a imagem está em seu pc, ex:D:\\Downloads\\fatorial.png
    time.sleep(3)
    campo_but = driver.find_element_by_xpath("//div[@class='SncVf _3doiV']")
    time.sleep(2)
    campo_but.click()   #enviando msg com img
    time.sleep(2)
    
#loop para enviar para todos os contatos 
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

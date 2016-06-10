from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import json
import random

class FacebookMap(object):

	def __init__(self, browser):
		self.browser = browser


	def Logar(self, usuario, senha):
		self.browser.get('http://facebook.com')

		txtEmail = self.browser.find_element_by_id('email')
		txtEmail.send_keys(usuario)

		txtSenha = self.browser.find_element_by_id('pass')
		txtSenha.send_keys(senha)

		btnEntrar = self.browser.find_element_by_id('u_0_m')
		btnEntrar.click()

	def EnviarParabens(self):
		try:
			with open('resource.json') as data_file:
				data = json.load(data_file)
		except:
			print("Você precisa ter um arquivo de mensagens de parabéns resource.json")
			data = []
			data.append("Feliz aniversário %s tudo de bom e felicidades :)")

		self.browser.get('https://www.facebook.com/events/birthdays')
		nomes_aniversariantes = self.browser.find_elements_by_class_name('_3ng2')
		nomes = []
		for pessoa in nomes_aniversariantes:
			if 'anos' not in pessoa.text or 'Ver' not in pessoa.text or 'Você':
				nomes.append(pessoa.text)

		texts_boxes = self.browser.find_elements_by_class_name('uiTextareaNoResize')
		x = 0
		for text_box in texts_boxes:
			if(x <= len(texts_boxes)):
				mensagem = data[random.randrange(0,len(data))] % nomes[x]
				text_box.send_keys(mensagem)
				text_box.send_keys(Keys.RETURN)

			x += 1

	def Encerrar(self):
		self.browser.close()
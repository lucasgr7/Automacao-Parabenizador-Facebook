from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

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

	def AcessarAniversariantes(self):
		self.browser.get('https://www.facebook.com/events/birthdays')
		nomes_aniversariantes = self.browser.find_elements_by_class_name('_3ng2')
		nomes = []
		for pessoa in nomes_aniversariantes:
			if 'anos' not in pessoa.text or 'Ver' not in pessoa.text or 'Você':
				nomes.append(pessoa.text)

		texts_boxes = self.browser.find_elements_by_class_name('uiTextareaNoResize')
		x = 1
		for text_box in texts_boxes:
			if(x <= len(texts_boxes)):
				text_box.send_keys('Feliz aniversário ' + nomes[x] + " tudo de bom e felicidades :)")
				text_box.send_keys(Keys.RETURN)

			x += 1

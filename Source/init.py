from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Mapping import FacebookMap


browser = webdriver.Firefox()
proc = FacebookMap(browser)
proc.Logar('email','senha')
proc.EnviarParabens()
proc.Encerrar()
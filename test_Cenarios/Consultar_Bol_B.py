from cgitb import text
from select import select
from turtle import title
import unittest
import time
from appium import webdriver
from numpy import set_string_function
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import date
from datetime import datetime
from selenium.webdriver.support.select import Select
from datetime import timedelta
from selenium.webdriver.common.action_chains import ActionChains


desired_capabilities = {
    'platformName': 'Android',
    'deviceName': 'samsung SM-A015M',
    'appPackage': 'br.com.boletins',
    "platformVersion": "11",
    'app': 'c:/automação/app-release-qa.apk'


}

driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desired_capabilities)
class TestLogin(unittest.TestCase):
 autenticadoSucesso = False
 autenticando = False
 loginSSO = False
 print("Iniciando Testes Automatizados")
 print("Iniciando Login no App")

 for x in range (2):
    print("Tentativa de Login número: " + str(x) )
    if autenticadoSucesso == True:
        break
    if x == 2:
       print ("****** NÃO FOI POSSÍVEL REALIZAR LOGIN  ******")
       exit()

    try:
     entrar = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Entrar']")
     entrar.click()
     time.sleep(5)
    except:
     pass

    try:
     print ("Entrou no Try linha 53")
     autenticando = driver.find_element(By.XPATH, "//android.view.View[@content-desc='Autenticando...']/android.view.View/android.view.View/android.widget.ScrollView/android.view.View")
     autenticando = True
     print ("Usuário autenticado, aguardando conclusão")
     time.sleep(40)
    except:
       pass

    if autenticando == False:
     try:
      print ("Entrou no try linha 63")
      loginSSO = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
      loginSSO = True
     except:
       pass

    if autenticadoSucesso == False and loginSSO == True: 
     try:
         print("Entrou no Try linha 71")
         estado_login = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]").is_enabled()
         print("Acesso Não Autenticado, Realizando Login")
          #inserir login e senha nos campos abaixo, itens removidos para subida em github 
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
          (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"))).send_keys('')
         senhasso = driver.find_element(
          By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]").send_keys('')
         entrarsso = driver.find_element(
          By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button").click()
         time.sleep(5)
         autenticando = True
         print ("Informações de login inseridas. 40s - linha 82")
         time.sleep(45)
     except:
        pass
     
     if autenticando == True:
      try:
       print("Entrou no Try linha 89")
       autenticadoSucesso = driver.find_element(By.XPATH,"//android.view.View[@content-desc='Boletins']")
       autenticadoSucesso = True
       print("timesleep 5 seg - linha 92")
       time.sleep(5)
       print ("Autenticado com sucesso, encerrando login")
      except: 
       pass
    
     if autenticadoSucesso == False:
      driver.launch_app()
    
print("Login realizado com sucesso, encerrando método Logon")

class testConsultaBolB(unittest.TestCase):
    ## Setando guia atual + nome do arquivo na evidência
    ts = time.strftime ("%d_%m_%Y_%H%M%S")
    activityname = driver.current_activity
    nomearquivo = activityname+ts

    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//android.view.View[@content-desc='Boletins']"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//android.view.View[@content-desc='Consultar']/android.view.View"))).click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//android.widget.Button[@content-desc='Editar']")))
    driver.save_screenshot("C:/automação/appium-practices-master/Screenshots/"+ts+"Consulta.png")
    print("Evidência Salva" + ts)
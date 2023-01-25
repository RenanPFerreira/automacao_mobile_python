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
from datetime import datetime, timedelta
from datetime import datetime
from selenium.webdriver.support.select import Select
from datetime import timedelta
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from sys import exit



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
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
          (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"))).send_keys('12345678910')
         senhasso = driver.find_element(
          By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]").send_keys('qa123')
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
    
class testEdicaoBol1(unittest.TestCase):
    ts = time.strftime ("%d_%m_%Y_%H%M%S") ## config para impressão do timestamp da evidência
         # Setando variáveis referente a HORA
    horaAtual = datetime.now()
    horaAtualEditada = horaAtual.strftime("%H:00")
    
    #h = 2
    #hf = 4

    horaInicioEditada = (horaAtual + timedelta(hours=2)).strftime('%H:00') 
    horaFinalEditada = (horaAtual + timedelta(hours=4)).strftime('%H:00')
    horaAtualEditadaH = horaAtual.strftime("%H")
    if horaFinalEditada == 24:
        horaFinalEditada = 00
        print ("Hora final editada para 00:00 ")        
    else:
        print("Hora final não alterada")

    print ("Somente Hora: " + str(horaAtualEditadaH))
    print ("Hora Atual Editada com :00: " + str(horaAtualEditada))
    print ("Hora Inicio Editada e com +2 horas: " + str(horaInicioEditada))
    print ("Hora Final Editada e com +4 horas: " + str(horaFinalEditada))


    WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
        (By.XPATH, "//android.view.View[@content-desc='Boletins']"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//android.view.View[@content-desc='Consultar']/android.view.View"))).click()
    time.sleep(25)
    # Edição da Hora (Adicionando +2h em cada campo)
    clickeditar = driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Editar']")
    clickeditar.click()
    time.sleep(20)
    clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
    clickProximo.click()
    time.sleep(5)
    ############################### Clique no Dropdown de Hora Inicio
    menuHoraInicio = driver.find_element(By.XPATH, "//android.widget.Button[contains(@content-desc,'Hora Início')]")
    menuHoraInicio.click()
    if int(horaAtualEditadaH) >= 12:
        driver.swipe(257, 1300, 257, 173)
    else:
        print("Hora atual menor que 12:00")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.ACCESSIBILITY_ID, str(horaInicioEditada)))).click()
    
    ############################### Clique no Dropdown de Hora Final 
    menuHoraFinal = driver.find_element(By.XPATH, "//android.widget.Button[contains(@content-desc,'Hora Fim')]")
    menuHoraFinal.click()

    if int(horaAtualEditadaH) >= 12:
            driver.swipe(622, 1300, 617, 149)
    else:
      print("Hora atual menor que 12:00")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
              (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
    time.sleep(2)
    campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
    campoOBS.click()
    campoOBS.send_keys('Edição de hora via Automação')
    driver.press_keycode(4)
    time.sleep(2)
    botaoEditar = driver.find_element(By. XPATH, "//android.widget.Button[@content-desc='Editar']")
    botaoEditar.click()
    ############################### Clique na confirmação da Edição
    confirmaEdicao = driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
    confirmaEdicao.click()
    time.sleep(5)
    driver.save_screenshot("C:/automação/appium-practices-master/Screenshots/"+ts+"Edição.png")
    print("Evidência Salva" + ts)
    print("Edição realizada via Automação")

class testEdicaoBol2 (unittest.TestCase):
    ts = time.strftime ("%d_%m_%Y_%H%M%S") ## config para impressão do timestamp da evidência
    print("Iniciando segunda edição de boletim")
    time.sleep(15)
    driver.swipe(527, 986, 518, 634)
    driver.implicitly_wait(2)
    time.sleep(5)
    driver.tap([(162,1004)],500)
   ## erro no método 
   ## clickeditar = driver.find_element((By.XPATH, "//android.widget.Button[@content-desc='Editar'])[2]"))            
   ## clickeditar.click()
    time.sleep(17)
    # Selecionar Motivo da Restrição
    print("Procurando Motivo Boletim Serviços...")
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo\nBOLETIM DE SERVIÇOS"))).click()
    time.sleep(5)
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "PROSSIGA COM ATENÇÃO"))).click()
    time.sleep(2)
    clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
    clickProximo.click()
    time.sleep(5)
    campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
    campoOBS.click()
    campoOBS.send_keys('Edição de motivo para Prossiga com Atenção via Automação')
    driver.press_keycode(4)
    time.sleep(2)
    botaoEditar = driver.find_element(By. XPATH, "//android.widget.Button[@content-desc='Editar']")
    botaoEditar.click()
    ############################### Clique na confirmação da Edição
    confirmaEdicao = driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
    confirmaEdicao.click()
    time.sleep(5)
    driver.save_screenshot("C:/automação/appium-practices-master/Screenshots/"+ts+"Edição.png")
    print("Evidência Salva" + ts)
    print("Edição realizada via Automação")
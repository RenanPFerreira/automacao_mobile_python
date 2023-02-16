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
from fixtures import dados


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

class TestCadastroBoletimCenario01(unittest.TestCase):
            print("Iniciando Cenário 01....")
            ## Setando timestamp evidência
            ts = time.strftime ("%d_%m_%Y_%H%M%S")
            print("Autenticação Realizada, Iniciando Cadastro")
            # clickBoletim = driver.find_element(By.XPATH,"//android.view.View[@content-desc='Boletins']")
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
            (By.XPATH, "//android.view.View[@content-desc='Boletins']"))).click()
            time.sleep(2)
            clickCadastrar = driver.find_element(
               By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View").click()
            time.sleep(20)
        # Cadastro de Boletins PT1
        # Selecionar Dropdown do Motivo 
            motivo = WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo")))
            motivo.click()
            time.sleep(13)
       # selecionardropdownMotivo = driver.find_element(By.ACCESSIBILITY_ID,"Motivo")
       # selecionardropdownMotivo.click()

        # Selecionar Motivo da Restrição
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "BOLETIM DE SERVIÇOS"))).click()
        # selecionarmotivo = driver.find_element(By.ACCESSIBILITY_ID,"RONDA")
        # selecionarmotivo.click()
        # time.sleep(5)
        # Selecionar Dropdown do Tipo da Restrição
            clickTipo = driver.find_element(
                By.XPATH, "//android.widget.Button[@content-desc='Tipo']").click()
            time.sleep(1)
        # Selecionar o Tipo da Restrição
            clickTipoRest = driver.find_element(
                By.XPATH, "//android.view.View[@content-desc='PROGRAMADO']").click()
        # Inserir informação da OS
            inserirOS = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            inserirOS.click()
            time.sleep(2)
            inserirOS.send_keys('000')
            driver.press_keycode(4)
            time.sleep(3)
        # Inserir nome da Turma
            nomeTurma = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            nomeTurma.click()
            time.sleep(2)
            nomeTurma.send_keys('QA AUTOMAÇÃO TESTE')
            driver.press_keycode(4)
            time.sleep(2)
            # Clicar no botão Próximo
            clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
            clickProximo.click()
        # Cadastro de Boletins PT2
            horaAtual = datetime.now()
            horaAtualEditadaH = horaAtual.strftime("%H")
            horaAtualEditada = horaAtual.strftime("%H:00")
           
            horaFinalEditada = (horaAtual + timedelta(hours=1)).strftime('%H:00')
            print("Hora Inicial Formatada: " + str(horaAtualEditada))
            print("Hora Final Formatada: " + str(horaFinalEditada))
            
   
            menuHoraInicio = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Início").click()

        # CONDIÇÃO SE HORA FOR MAIOR QUE 12H REALIZAR DROPDOWN NO HORA INÍCIO
            if int(horaAtualEditadaH) >= 12:
                driver.swipe(257, 1300, 257, 173)
            else:
                print("Hora atual menor que 12:00")
            
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID,str(horaAtualEditada)))).click()
            
            menuHoraFinal = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Fim").click()

            if int(horaAtualEditadaH) >= 12:
                driver.swipe(622, 1300, 617, 149)
            else:
                print("Hora atual menor que 12:00")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
            

        # Dropdown Subdivisão e Selecionar Sub 73

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Subdivisão"))).click()
            time.sleep(2)
        # def test_scroll(driver):
            for x in range(15):
             try:
                subdivisao = driver.find_element(By.ACCESSIBILITY_ID, "73 - ARARAQUARA - MARCO INICIAL").is_displayed()
                if subdivisao is True:
                    break
             except:
                 #swipe na tela de trechos
                 driver.swipe(595, 1208, 591, 500)
                 driver.implicitly_wait(2)
             continue

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "73 - ARARAQUARA - MARCO INICIAL"))).click()
        # Dropdown Linha e Selecionar Principal
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Linha"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Principal"))).click()
        # Campo KM Inicial e KM Final e Observação

       # kmInicial = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            kmInicial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")))
            kmInicial.click()
            time.sleep(2)
            kmInicial.send_keys('36.500')
            driver.execute_script(
            'mobile: performEditorAction', {'action': 'next'})

            kmFinal = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
            kmFinal.click()
            time.sleep(2)
            kmFinal.send_keys('39.500')
            time.sleep(2)
            driver.hide_keyboard()
            ##driver.execute_script(
            ##'mobile: performEditorAction', {'action': 'next'})
            time.sleep(2)
            campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
            #campoOBS = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            campoOBS.click()
            campoOBS.send_keys('Restrição Inserida via Automação')
            driver.press_keycode(4)
            time.sleep(2)
               # TryCatch para o botão Cadastrar
            cadastrousucesso = False
            for y in range(1):
             
             if cadastrousucesso is True:
              break
             if y == 1:
                print ("Falha ao cadastrar o boletim, realizado " +str(y) + " tentativas sem sucesso.")
                #Pesquisar para setar teste como falha
                break 
             try:
                print("Entrou no TryCatch Linha 250")
                clickCadastrarRest = driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Cadastrar']")
                time.sleep(2)
                clickCadastrarRest.click()
                time.sleep(2)
                botaoOkRest = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
                botaoOkRest.click() 
                time.sleep(20)
                print("Aguardando time sleep de 20s")
                cadastrousucesso = driver.find_element((By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View"))
                cadastrousucesso = True
                break              
             except:
                pass
            print("Boletim Cadastrado com sucesso, finalizando cenário 01")      
class TestCadastroBoletimCenario02(unittest.TestCase):
            print("Iniciando Cenário 02...")
            print("Aguardando elemento ficar disponível...")
            time.sleep(15)         
            ## Setando timestamp evidência
            ts = time.strftime ("%d_%m_%Y_%H%M%S")
            print("Autenticação Realizada, Iniciando Cadastro Cenário 02")
            clickCadastrar = driver.find_element(
               By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View").click()
            time.sleep(20)
        # Cadastro de Boletins PT1
        # Selecionar Dropdown do Motivo
            motivo = WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo")))
            motivo.click()
            time.sleep(2)
       # selecionardropdownMotivo = driver.find_element(By.ACCESSIBILITY_ID,"Motivo")
       # selecionardropdownMotivo.click()

        # Selecionar Motivo da Restrição
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "BOLETIM DE SERVIÇOS"))).click()
        # selecionarmotivo = driver.find_element(By.ACCESSIBILITY_ID,"RONDA")
        # selecionarmotivo.click()
        # time.sleep(5)
        # Selecionar Dropdown do Tipo da Restrição
            clickTipo = driver.find_element(
                By.XPATH, "//android.widget.Button[@content-desc='Tipo']").click()
            time.sleep(1)
        # Selecionar o Tipo da Restrição
            clickTipoRest = driver.find_element(
                By.XPATH, "//android.view.View[@content-desc='ESPECIAL']").click()
        # Inserir informação da OS
            inserirOS = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            inserirOS.click()
            time.sleep(2)
            inserirOS.send_keys('000')
            driver.press_keycode(4)
            time.sleep(3)
        # Inserir nome da Turma
            nomeTurma = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            nomeTurma.click()
            time.sleep(2)
            nomeTurma.send_keys('QA AUTOMAÇÃO TESTE')
            driver.press_keycode(4)
            # Clicar no botão Próximo
            clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
            clickProximo.click()
        
         # Cadastro de Boletins PT2
            horaAtual = datetime.now()
            horaAtualEditadaH = horaAtual.strftime("%H")
            horaAtualEditada = horaAtual.strftime("%H:00")
           
            horaFinalEditada = (horaAtual + timedelta(hours=1)).strftime('%H:00')
            print("Hora Inicial Formatada: " + str(horaAtualEditada))
            print("Hora Final Formatada: " + str(horaFinalEditada))
            
   
            menuHoraInicio = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Início").click()

        # CONDIÇÃO SE HORA FOR MAIOR QUE 12H REALIZAR DROPDOWN NO HORA INÍCIO
            if int(horaAtualEditadaH) >= 12:
                driver.swipe(257, 1300, 257, 173)
            else:
                print("Hora atual menor que 12:00")
            
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID,str(horaAtualEditada)))).click()
            
            menuHoraFinal = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Fim").click()

            if int(horaAtualEditadaH) >= 12:
                driver.swipe(622, 1300, 617, 149)
            else:
                print("Hora atual menor que 12:00")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
            

        # Dropdown Subdivisão e Selecionar Sub 73

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Subdivisão"))).click()
            time.sleep(2)
        # def test_scroll(driver):
            for x in range(15):
             try:
                subdivisao = driver.find_element(By.ACCESSIBILITY_ID, "54 - EVANGELISTA DE SOUZA - PARATINGA (L1 PRINCIPAL)").is_displayed()
                if subdivisao is True:
                    break
             except:
                 #swipe na tela de trechos
                 driver.swipe(595, 1208, 591, 500)
                 driver.implicitly_wait(2)
             continue

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "54 - EVANGELISTA DE SOUZA - PARATINGA (L1 PRINCIPAL)"))).click()
        # Dropdown Linha e Selecionar Principal
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Linha"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Principal"))).click()
        # Campo KM Inicial e KM Final e Observação

       # kmInicial = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            kmInicial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")))
            kmInicial.click()
            time.sleep(2)
            kmInicial.send_keys('98.000')
            driver.execute_script(
            'mobile: performEditorAction', {'action': 'next'})

            kmFinal = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
            kmFinal.click()
            time.sleep(2)
            kmFinal.send_keys('100.000')
            time.sleep(2)
            driver.hide_keyboard()
            ##driver.execute_script(
            ##'mobile: performEditorAction', {'action': 'next'})
            time.sleep(2)
            campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
            #campoOBS = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            campoOBS.click()
            campoOBS.send_keys('Restrição via Automação Mobile - CN02 - ZGPZWU1 - PORTOFER')
            driver.press_keycode(4)
            cadastrousucesso = False
            y = 0
            for y in range(1):
             if cadastrousucesso is True:
              break
             if y == 1:
                print ("Falha ao cadastrar o boletim, realizado " +str(y) + " tentativas sem sucesso.")
                #Pesquisar para setar teste como falha
                break 
             try:
                print("Entrou no TryCatch Linha 411")
                clickCadastrarRest = driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Cadastrar']")
                time.sleep(2)
                clickCadastrarRest.click()
                time.sleep(2)
                botaoOkRest = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
                botaoOkRest.click() 
                time.sleep(20)
                print("Aguardando time sleep de 20s")
                cadastrousucesso = driver.find_element((By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View"))
                cadastrousucesso = True
                break              
             except:
                pass
            print("Boletim Cadastrado, Finalizando cenário 02...")              
class TestCadastroBoletimCenario03(unittest.TestCase):           
            print("Iniciando Cenário 03...")
            print("Aguardando elemento ficar disponível...")
            time.sleep(15)
            ## Setando timestamp evidência
            ts = time.strftime ("%d_%m_%Y_%H%M%S")
            print("Autenticação Realizada, Iniciando Cadastro Cenário 03")
            time.sleep(2)
            clickCadastrar = driver.find_element(
               By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View").click()
            time.sleep(20)
        # Cadastro de Boletins PT1
        # Selecionar Dropdown do Motivo
            motivo = WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo")))
            motivo.click()
            time.sleep(2)
       # selecionardropdownMotivo = driver.find_element(By.ACCESSIBILITY_ID,"Motivo")
       # selecionardropdownMotivo.click()

        # Selecionar Motivo da Restrição
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "BOLETIM DE SERVIÇOS"))).click()
        # selecionarmotivo = driver.find_element(By.ACCESSIBILITY_ID,"RONDA")
        # selecionarmotivo.click()
        # time.sleep(5)
        # Selecionar Dropdown do Tipo da Restrição
            clickTipo = driver.find_element(
                By.XPATH, "//android.widget.Button[@content-desc='Tipo']").click()
            time.sleep(1)
        # Selecionar o Tipo da Restrição
            clickTipoRest = driver.find_element(
                By.XPATH, "//android.view.View[@content-desc='EMERGENCIAL']").click()
        # Inserir informação da OS
            inserirOS = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            inserirOS.click()
            time.sleep(2)
            inserirOS.send_keys('000')
            driver.press_keycode(4)
            time.sleep(3)
        # Inserir nome da Turma
            nomeTurma = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            nomeTurma.click()
            time.sleep(2)
            nomeTurma.send_keys('QA AUTOMAÇÃO TESTE')
            driver.press_keycode(4)
            # Clicar no botão Próximo
            clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
            clickProximo.click()
         # Cadastro de Boletins PT2
            horaAtual = datetime.now()
            
            horaAtualEditada = horaAtual.strftime("%H:00")
            horaAtualEditadaH = horaAtual.strftime("%H")
            horaFinalEditada = (horaAtual + timedelta(hours=1)).strftime('%H:00')
            print("Hora Inicial Formatada: " + str(horaAtualEditada))
            print("Hora Final Formatada: " + str(horaFinalEditada))
            
   
            menuHoraInicio = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Início").click()

        # CONDIÇÃO SE HORA FOR MAIOR QUE 12H REALIZAR DROPDOWN NO HORA INÍCIO
            if int(horaAtualEditadaH) >= 12:
                driver.swipe(257, 1300, 257, 173)
            else:
                print("Hora atual menor que 12:00")
            
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID,str(horaAtualEditada)))).click()
            
            menuHoraFinal = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Fim").click()

            if int(horaAtualEditadaH) >= 12:
                driver.swipe(622, 1300, 617, 149)
            else:
                print("Hora atual menor que 12:00")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
            

        # Dropdown Subdivisão e Selecionar Sub 73

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Subdivisão"))).click()
            time.sleep(2)
        # def test_scroll(driver):
            for x in range(15):
             try:
                subdivisao = driver.find_element(By.ACCESSIBILITY_ID, "54 - EVANGELISTA DE SOUZA - PARATINGA (L1 PRINCIPAL)").is_displayed()
                if subdivisao is True:
                    break
             except:
                 #swipe na tela de trechos
                 driver.swipe(595, 1208, 591, 500)
                 driver.implicitly_wait(2)
             continue

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "54 - EVANGELISTA DE SOUZA - PARATINGA (L1 PRINCIPAL)"))).click()
        # Dropdown Linha e Selecionar Principal
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Linha"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Principal"))).click()
        # Campo KM Inicial e KM Final e Observação

       # kmInicial = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            kmInicial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")))
            kmInicial.click()
            time.sleep(2)
            kmInicial.send_keys('72.000')
            driver.execute_script(
            'mobile: performEditorAction', {'action': 'next'})

            kmFinal = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
            kmFinal.click()
            time.sleep(2)
            kmFinal.send_keys('73.000')
            time.sleep(2)
            driver.hide_keyboard()
            ##driver.execute_script(
            ##'mobile: performEditorAction', {'action': 'next'})
            time.sleep(2)
            campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
            #campoOBS = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            campoOBS.click()
            campoOBS.send_keys('Restrição via Automação Mobile - CN03 - ZEZ1 - PORTOFER')
            driver.press_keycode(4)
            time.sleep(2)
            cadastrousucesso = False
            y = 0
            for y in range(1):
             if cadastrousucesso is True:
              break
             if y == 1:
                print ("Falha ao cadastrar o boletim, realizado " +str(y) + " tentativas sem sucesso.")
                #Pesquisar para setar teste como falha
                break 
             try:
                print("Entrou no TryCatch Linha 572")
                clickCadastrarRest = driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Cadastrar']")
                time.sleep(2)
                clickCadastrarRest.click()
                time.sleep(2)
                botaoOkRest = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
                botaoOkRest.click() 
                time.sleep(20)
                print("Aguardando time sleep de 20s")
                cadastrousucesso = driver.find_element((By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View"))
                cadastrousucesso = True
                break              
             except:
                pass
            print("Boletim Cadastrado, Finalizando cenário 03...")            
class TestCadastroBoletimCenario04(unittest.TestCase):
            print("Iniciando Cenário 04...")
            print("Aguardando elemento ficar disponível...")
            time.sleep(15)
            ## Setando timestamp evidência
            ts = time.strftime ("%d_%m_%Y_%H%M%S")
            print("Autenticação Realizada, Iniciando Cadastro Cenário 04")
            clickCadastrar = driver.find_element(
               By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View").click()
            time.sleep(20)
        # Cadastro de Boletins PT1
        # Selecionar Dropdown do Motivo
            motivo = WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo")))
            motivo.click()
            time.sleep(2)
       # selecionardropdownMotivo = driver.find_element(By.ACCESSIBILITY_ID,"Motivo")
       # selecionardropdownMotivo.click()

        # Selecionar Motivo da Restrição
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "BOLETIM DE SERVIÇOS"))).click()
        # selecionarmotivo = driver.find_element(By.ACCESSIBILITY_ID,"RONDA")
        # selecionarmotivo.click()
        # time.sleep(5)
        # Selecionar Dropdown do Tipo da Restrição
            clickTipo = driver.find_element(
                By.XPATH, "//android.widget.Button[@content-desc='Tipo']").click()
            time.sleep(1)
        # Selecionar o Tipo da Restrição
            clickTipoRest = driver.find_element(
                By.XPATH, "//android.view.View[@content-desc='EMERGENCIAL']").click()
        # Inserir informação da OS
            inserirOS = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            inserirOS.click()
            time.sleep(2)
            inserirOS.send_keys('000')
            driver.press_keycode(4)
        # Inserir nome da Turma
            nomeTurma = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            nomeTurma.click()
            time.sleep(2)
            nomeTurma.send_keys('QA AUTOMAÇÃO TESTE')
            driver.press_keycode(4)
            # Clicar no botão Próximo
            clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
            clickProximo.click()
         # Cadastro de Boletins PT2
            horaAtual = datetime.now()
            horaAtualEditada = horaAtual.strftime("%H:00")
            horaAtualEditadaH = horaAtual.strftime("%H")
            horaFinalEditada = (horaAtual + timedelta(hours=1)).strftime('%H:00')
            print("Hora Inicial Formatada: " + str(horaAtualEditada))
            print("Hora Final Formatada: " + str(horaFinalEditada))
            
   
            menuHoraInicio = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Início").click()

        # CONDIÇÃO SE HORA FOR MAIOR QUE 12H REALIZAR DROPDOWN NO HORA INÍCIO
            if int(horaAtualEditadaH) >= 12:
                driver.swipe(257, 1300, 257, 173)
            else:
                print("Hora atual menor que 12:00")
            
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID,str(horaAtualEditada)))).click()
            
            menuHoraFinal = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Fim").click()

            if int(horaAtualEditadaH) >= 12:
                driver.swipe(622, 1300, 617, 149)
            else:
                print("Hora atual menor que 12:00")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
            

        # Dropdown Subdivisão e Selecionar Sub 73

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Subdivisão"))).click()
            time.sleep(2)
        # def test_scroll(driver):
            for x in range(15):
             try:
                subdivisao = driver.find_element(By.ACCESSIBILITY_ID, "54 - EVANGELISTA DE SOUZA - PARATINGA (L1 PRINCIPAL)").is_displayed()
                if subdivisao is True:
                    break
             except:
                 #swipe na tela de trechos
                 driver.swipe(595, 1208, 591, 500)
                 driver.implicitly_wait(3)
             continue

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "54 - EVANGELISTA DE SOUZA - PARATINGA (L1 PRINCIPAL)"))).click()
        # Dropdown Linha e Selecionar Principal
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Linha"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Principal"))).click()
        # Campo KM Inicial e KM Final e Observação

       # kmInicial = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            kmInicial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")))
            kmInicial.click()
            time.sleep(2)
            kmInicial.send_keys('82.000')
            driver.execute_script(
            'mobile: performEditorAction', {'action': 'next'})

            kmFinal = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
            kmFinal.click()
            time.sleep(2)
            kmFinal.send_keys('82.300')
            time.sleep(2)
            driver.hide_keyboard()
            ##driver.execute_script(
            ##'mobile: performEditorAction', {'action': 'next'})
            time.sleep(2)
            campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
            #campoOBS = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            campoOBS.click()
            campoOBS.send_keys('Restrição via Automação Mobile - CN04 - ZXW1 - PORTOFER')
            driver.press_keycode(4)
            time.sleep(2)
            cadastrousucesso = False
            y = 0
            for y in range(1):
             if cadastrousucesso is True:
              break
             if y == 1:
                print ("Falha ao cadastrar o boletim, realizado " +str(y) + " tentativas sem sucesso.")
                #Pesquisar para setar teste como falha
                break 
             try:
                print("Entrou no TryCatch Linha 732")
                clickCadastrarRest = driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Cadastrar']")
                time.sleep(2)
                clickCadastrarRest.click()
                time.sleep(2)
                botaoOkRest = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
                botaoOkRest.click() 
                time.sleep(20)
                print("Aguardando time sleep de 20s")
                cadastrousucesso = driver.find_element((By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View"))
                cadastrousucesso = True
                break              
             except:
                pass
            print("Boletim Cadastrado, Finalizando cenário 04")
class TestCadastroBoletimCenario05(unittest.TestCase):
            print("Iniciando cadastro de Boletim em 5s")
            time.sleep(5)
            print("Iniciando Cenário 05...")
            ## Setando timestamp evidência
            ts = time.strftime ("%d_%m_%Y_%H%M%S")
            #clickBoletim = driver.find_element(By.XPATH,"//android.view.View[@content-desc='Boletins']")
           # WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
           # (By.XPATH, "//android.view.View[@content-desc='Boletins']"))).click()
           # time.sleep(2)
           # print("Autenticação Realizada, Iniciando Cadastro Cenário 05")
            clickCadastrar = driver.find_element(
               By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View").click()
            time.sleep(20)
        # Cadastro de Boletins PT1
        # Selecionar Dropdown do Motivo
            print ("*****Clicando no Motivo")
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo"))).click()
            #motivo.click()
            #time.sleep(6)
            # Selecionar Motivo da Restrição
            print("*****Selecionando Motivo")
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "RONDA"))).click()
            print("*****Aguardando 6s")
            time.sleep(6)
        # Selecionar Dropdown do Tipo da Restrição
            print("*****Selecionando tipo")
            clickTipo = driver.find_element(
                By.XPATH, "//android.widget.Button[@content-desc='Tipo']").click()
            time.sleep(1)
        # Selecionar o Tipo da Restrição
            clickTipoRest = driver.find_element(
                By.XPATH, "//android.view.View[@content-desc='EMERGENCIAL']").click()
        # Inserir informação da OS
            inserirOS = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            inserirOS.click()
            time.sleep(2)
            print("*****Preenchendo OS")
            inserirOS.send_keys('000')
            driver.press_keycode(4)
            selecionarCDT =  WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"))).click()
            time.sleep(1)
            print("*****Removendo e informando CDT Ronda")
            removerCDT = driver.find_element(
                By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText/android.widget.Button")
            removerCDT.click()
            time.sleep(1)
            preencherCDT = WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
               (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText")))
            time.sleep(1)
            preencherCDT.click()
            preencherCDT.send_keys("RONDA")
            time.sleep(1)
            driver.tap([(215,410)],500)

            """clicarOK = driver.find_element(
                By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
            clicarOK.click()"""

            time.sleep(1)
        # Inserir nome da Turma
            print("*****Informando turma")
            nomeTurma = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            nomeTurma.click()
            time.sleep(2)
            nomeTurma.send_keys('QA AUTOMAÇÃO TESTE')
            driver.press_keycode(4)
            time.sleep(3)
            # Clicar no botão Próximo
            clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
            clickProximo.click()
         # Cadastro de Boletins PT2
            horaAtual = datetime.now()
            horaAtualEditadaH = horaAtual.strftime("%H")
            horaAtualEditada = horaAtual.strftime("%H:00")
           
            horaFinalEditada = (horaAtual + timedelta(hours=1)).strftime('%H:00')
            print("Hora Inicial Formatada: " + str(horaAtualEditada))
            print("Hora Final Formatada: " + str(horaFinalEditada))
            
   
            menuHoraInicio = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Início").click()

        # CONDIÇÃO SE HORA FOR MAIOR QUE 12H REALIZAR DROPDOWN NO HORA INÍCIO
            if int(horaAtualEditadaH) >= 12:
                driver.swipe(257, 1300, 257, 173)
            else:
                print("Hora atual menor que 12:00")
            
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID,str(horaAtualEditada)))).click()
            
            menuHoraFinal = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Fim").click()

            if int(horaAtualEditadaH) >= 12:
                driver.swipe(622, 1300, 617, 149)
            else:
                print("Hora atual menor que 12:00")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
            

        # Dropdown Subdivisão e Selecionar Sub 73

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Subdivisão"))).click()
            time.sleep(2)
        # def test_scroll(driver):
            for x in range(15):
             try:
                subdivisao = driver.find_element(By.ACCESSIBILITY_ID, "10 - PARANAGUÁ - IGUAÇU").is_displayed()
                if subdivisao is True:
                    break
             except:
                 #swipe na tela de trechos
                 driver.swipe(595, 1208, 591, 500)
                 driver.implicitly_wait(2)
             continue

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "10 - PARANAGUÁ - IGUAÇU"))).click()
        # Dropdown Linha e Selecionar Principal
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Linha"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Desviada"))).click()
        # Campo KM Inicial e KM Final e Observação

       # kmInicial = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            kmInicial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")))
            kmInicial.click()
            time.sleep(2)
            kmInicial.send_keys('50.289')
            driver.execute_script(
            'mobile: performEditorAction', {'action': 'next'})

            kmFinal = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
            kmFinal.click()
            time.sleep(2)
            kmFinal.send_keys('51.046')
            time.sleep(2)
            driver.hide_keyboard()
            ##driver.execute_script(
            ##'mobile: performEditorAction', {'action': 'next'})
            time.sleep(1)
            campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
            #campoOBS = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            campoOBS.click()
            campoOBS.send_keys('Restrição via Automação Mobile - CN05 - LPCP - CTC')
            driver.press_keycode(4)
            time.sleep(2)
            cadastrousucesso = False
            y = 0
            for y in range(1):
             if cadastrousucesso is True:
              break
             if y == 1:
                print ("Falha ao cadastrar o boletim, realizado " +str(y) + " tentativas sem sucesso.")
                #Pesquisar para setar teste como falha
                break 
             try:
                print("Entrou no TryCatch Linha 918")
                clickCadastrarRest = driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Cadastrar']")
                time.sleep(2)
                clickCadastrarRest.click()
                time.sleep(2)
                botaoOkRest = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
                botaoOkRest.click() 
                time.sleep(20)
                print("Aguardando time sleep de 20s")
                cadastrousucesso = driver.find_element((By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View"))
                cadastrousucesso = True
                break              
             except:
                pass
            print("Boletim Cadastrado, Finalizando cenário 05...")
class TestCadastroBoletimCenario06(unittest.TestCase):
            print("Iniciando cadastro de Boletim em 5s")
            time.sleep(5)
            print("Iniciando Cenário 06...")
            ## Setando timestamp evidência
            ts = time.strftime ("%d_%m_%Y_%H%M%S")
            #clickBoletim = driver.find_element(By.XPATH,"//android.view.View[@content-desc='Boletins']")
            ##WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
            ##(By.XPATH, "//android.view.View[@content-desc='Boletins']"))).click()
            time.sleep(2)
            print("Autenticação Realizada, Iniciando Cadastro Cenário 06")
            ##inserir trycatch, se hora inferior a permitida add hora início e hora fim +1
            clickCadastrar = driver.find_element(
               By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View").click()
            time.sleep(20)
        # Cadastro de Boletins PT1
        # Selecionar Dropdown do Motivo
            print ("*****Clicando no Motivo")
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Motivo"))).click()
            #motivo.click()
            #time.sleep(6)
            # Selecionar Motivo da Restrição
            print("*****Selecionando Motivo")
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "BOLETIM DE SERVIÇOS"))).click()
            print("*****Aguardando 6s")
            time.sleep(6)
            print("*****Clicando no Pare Sim")
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
                (By.ACCESSIBILITY_ID, "Pare sim"))).click()
        # Selecionar Dropdown do Tipo da Restrição
            print("*****Selecionando tipo")
            clickTipo = driver.find_element(
                By.XPATH, "//android.widget.Button[@content-desc='Tipo']").click()
            time.sleep(1)
        # Selecionar o Tipo da Restrição
            clickTipoRest = driver.find_element(
                By.XPATH, "//android.view.View[@content-desc='EMERGENCIAL']").click()
        # Inserir informação da OS
            inserirOS = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            inserirOS.click()
            time.sleep(2)
            print("*****Preenchendo OS")
            inserirOS.send_keys('000')
            driver.press_keycode(4)

            """Funções  para preencher tipo Boletim Ronda"""    
            ##selecionarCDT =  WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
            ##    (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"))).click()
            ##time.sleep(1)
            ##print("*****Removendo e informando CDT Ronda")
            ##removerCDT = driver.find_element(
            ##    By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText/android.widget.Button")
            ##removerCDT.click()
            ##time.sleep(1)
            ##preencherCDT = WebDriverWait(driver, 40).until(EC.element_to_be_clickable(
            ##   (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView/android.widget.EditText")))
            ##time.sleep(1)
            ##preencherCDT.click()
            ##preencherCDT.send_keys("RONDA")
            ##time.sleep(1)
            ##driver.tap([(215,410)],500)

            time.sleep(1)
        # Inserir nome da Turma
            print("*****Informando turma")
            nomeTurma = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            nomeTurma.click()
            time.sleep(2)
            nomeTurma.send_keys('QA AUTOMAÇÃO TESTE')
            driver.press_keycode(4)
            time.sleep(3)
            # Clicar no botão Próximo
            clickProximo = driver.find_element(
            By.XPATH, "//android.widget.Button[@content-desc='Próximo']")
            clickProximo.click()
         # Cadastro de Boletins PT2
            horaAtual = datetime.now()
            horaAtualEditada = horaAtual.strftime("%H:00")
            horaAtualEditadaH = horaAtual.strftime("%H")
            horaFinalEditada = (horaAtual + timedelta(hours=1)).strftime('%H:00')
            print("Hora Inicial Formatada: " + str(horaAtualEditada))
            print("Hora Final Formatada: " + str(horaFinalEditada))
            
   
            menuHoraInicio = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Início").click()

        # CONDIÇÃO SE HORA FOR MAIOR QUE 12H REALIZAR DROPDOWN NO HORA INÍCIO
            if int(horaAtualEditadaH) >= 12:
                driver.swipe(257, 1300, 257, 173)
            else:
                print("Hora atual menor que 12:00")
            
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID,str(horaAtualEditada)))).click()
            
            menuHoraFinal = driver.find_element(
            By.ACCESSIBILITY_ID, "Hora Fim").click()

            if int(horaAtualEditadaH) >= 12:
                driver.swipe(622, 1300, 617, 149)
            else:
                print("Hora atual menor que 12:00")

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
             (By.ACCESSIBILITY_ID, str(horaFinalEditada)))).click()
            

        # Dropdown Subdivisão e Selecionar Sub 73

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Subdivisão"))).click()
            time.sleep(2)
        # def test_scroll(driver):
            for x in range(15):
             try:
                subdivisao = driver.find_element(By.ACCESSIBILITY_ID, "73 - ARARAQUARA - MARCO INICIAL").is_displayed()
                if subdivisao is True:
                    break
             except:
                 #swipe na tela de trechos
                 driver.swipe(595, 1208, 591, 500)
                 driver.implicitly_wait(2)
             continue

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "73 - ARARAQUARA - MARCO INICIAL"))).click()
        # Dropdown Linha e Selecionar Principal
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Linha"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.ACCESSIBILITY_ID, "Desviada"))).click()
        # Campo KM Inicial e KM Final e Observação

       # kmInicial = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
            kmInicial = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")))
            kmInicial.click()
            time.sleep(2)
            kmInicial.send_keys('24.000')
            driver.execute_script(
            'mobile: performEditorAction', {'action': 'next'})

            kmFinal = driver.find_element(
            By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]")
            kmFinal.click()
            time.sleep(2)
            kmFinal.send_keys('25.000')
            time.sleep(2)
            driver.hide_keyboard()
            ##driver.execute_script(
            ##'mobile: performEditorAction', {'action': 'next'})
            time.sleep(1)
            campoOBS = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")))
            #campoOBS = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]")
            campoOBS.click()
            campoOBS.send_keys('Restrição via Automação Mobile - CN06 - ZDZ1 - ARARAQUARA')
            driver.press_keycode(4)
            time.sleep(2)
            cadastrousucesso = False
            y = 0
            for y in range(1):
             if cadastrousucesso is True:
              break
             if y == 1:
                print ("Falha ao cadastrar o boletim, realizado " +str(y) + " tentativas sem sucesso.")
                #Pesquisar para setar teste como falha
                break 
             try:
                print("Entrou no TryCatch Linha 1104")
                clickCadastrarRest = driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Cadastrar']")
                time.sleep(2)
                clickCadastrarRest.click()
                time.sleep(2)
                botaoOkRest = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]")
                botaoOkRest.click() 
                time.sleep(20)
                print("Aguardando time sleep de 20s")
                cadastrousucesso = driver.find_element((By.XPATH, "//android.view.View[@content-desc='Cadastrar']/android.view.View"))
                cadastrousucesso = True
                break              
             except:
                pass
            print("Boletim Cadastrado,Finalizando cenário 06...")
            print("Finalizando cadastro de boletins....")


## Anotação Mental: 
## Terminar criação de Edição de boletins 
## pendente adicionar Try Except para mapear e tratar as exceções possíveis
          
if __name__ == '__main__':
    unittest.main()
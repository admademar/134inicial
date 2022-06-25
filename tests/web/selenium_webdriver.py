# Configura

from selenium import webdriver
from selenium.webdriver.common.by import By

    # Dados de Entrada
origen = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Jose Dunha do Teto '
local_address = 'Av Paulista, 000'
bandeira = 'American Express'
lembrar_de_mim = True

          # Resultados Esperados
        # verificação da pagina
titulo_passagens_esperada = 'Flights from São Paolo to New York:'
mensagem_de_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


        # Executa
class Testes:
         # Início

    def setup_method(self):

        # Instanciar a Biblioteca / motor / engine

        # Informar onde esta o WebDriver
        # Abrir o Chrome
        self.driver = webdriver.Chrome('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject\\134inicial\\venv\\Scripts\\chromedriver.exe')
        self.vars = {}


       #  Fim
    def teardown_method(self):

        # destruir o objeto da Biblioteca utilizada

        self.driver.quit()

        # Meio
    def testar_comprar_passagem(self):

        # Teste E2E / End to End / Ponta a Ponta
        # Abrir o site para automatizar get no endpoint /  virificação do titulo
        self.driver.get("https://www.blazedemo.com")
        self.driver.maximize_window()
        title = self.driver.title
        assert title == "BlazeDemo"
        print('************************')
        print('')
        print(f'PRIMEIRA TELA      ' + title + '.')

            # Executa / Valida
        # Pagina Inicial (Home)
        assert self.driver.find_element(By.XPATH, "//div[2]/div/h1").text == "Welcome to the Simple Travel Agency!"
        # Escolher a cidade de Origen e Click
        self.driver.find_element(By.XPATH, f'//option[.="São Paolo"]').click()
        # Escolher a cidade de Destino e Click
        self.driver.find_element(By.XPATH, f'//option[.="New York"]').click()
        self.driver.find_element(By.XPATH, "//input").click()
        title = self.driver.title
        assert title == "BlazeDemo - reserve"
        print('*******************************')
        print(f'SEGUNDA TELA       ' + title + '.')

        # Executa / Valida
        #Pagina Lista de Passagens

        assert self.driver.find_element(By.XPATH, "//div[2]/h3").text == titulo_passagens_esperada
        self.driver.find_element(By.XPATH, "//tr[1]/td[1]/input").click()
        title = self.driver.title
        assert title == "BlazeDemo Purchase"
        print('*******************************')
        print(f'TERCEIRA TELA      ' + title + '.')

        self.driver.find_element(By.ID, "inputName").send_keys("Dunha Caiu do Teto")
        self.driver.find_element(By.XPATH, "//input[@id='state']").send_keys("São Paulo/SP")
        self.driver.find_element(By.XPATH, "//input[@id='zipCode']").send_keys("99999999")
        self.driver.find_element(By.XPATH, '//*[@id="address"]').send_keys("Av Paulista, 000")
        self.driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Osasco City")
        self.driver.find_element(By.XPATH, "//option[3]").click()
        self.driver.find_element(By.CSS_SELECTOR, "#creditCardNumber").send_keys("9999.8888.7777.1111")
        self.driver.find_element(By.XPATH, "//input[@id='creditCardMonth']").send_keys("07")
        self.driver.find_element(By.CSS_SELECTOR, "#nameOnCard").send_keys("DinersDunha")
        self.driver.find_element(By.XPATH, "//input[@id='rememberMe']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.implicitly_wait(3000)
        # Executa / Valida
        # Pagina de Compra
        self.driver.find_element(By.XPATH, "//tr[3]//td[2]").text == preco_passagem_esperado

        # Executa / Valida
        # Pagina de Obrigado
        assert self.driver.find_element(By.XPATH, "//div[1]/h1").text == mensagem_de_agradecimento_esperada

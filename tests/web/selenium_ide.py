from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCompradepassagem:
    def setup_method(self):
        self.driver = webdriver.Chrome('C:\\Users\\ademarfr\\PycharmProjects\\pythonProject'
        '\\134inicial\\venv\\WebDriverManager\\chrome\\102.0.5005.61\\chromedriver_win32\\chromedriver.exe'
        )
        self.vars = {}

    def teardown_method(self):
         self.driver.quit()

    def test_compra_de_passagem(self):
        self.driver.get("https://www.blazedemo.com/")
        self.driver.set_window_size(1040, 744)
        self.driver.find_element(By.NAME, "fromPort").click()
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        self.driver.find_element(By.NAME, "toPort").click()
        dropdown = self.driver.find_element(By.NAME, "toPort")
        dropdown.find_element(By.XPATH, "//option[. = 'New York']").click()
        self.driver.find_element(By.XPATH, "//input['.btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)").text == "Airline: United"
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4)").text == "Price: 400"
        assert self.driver.find_element(By.CSS_SELECTOR, "em").text == "914.76"
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys("ademar")
        self.driver.find_element(By.ID, "rememberMe").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"

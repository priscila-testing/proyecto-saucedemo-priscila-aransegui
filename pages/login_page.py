from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:

    URL = "https://www.saucedemo.com/"

    _USERNAME = (By.ID, "user-name")
    _PASSWORD = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _PAGE_LOGO = (By.CLASS_NAME, "app_logo")
    _ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def ingresar_usuario(self, usuario):
        self.wait.until(EC.visibility_of_element_located(self._USERNAME)).send_keys(usuario)

    def ingresar_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self._PASSWORD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

    def login_completo(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def obtener_logo_pagina(self):
        return self.wait.until(EC.visibility_of_element_located(self._PAGE_LOGO))

    def obtener_error(self):
        try:
            error = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self._ERROR))
            return error.text
        except TimeoutException:
            return "No se encontró mensaje de error"

    def limpiar_campos(self):
        self.driver.find_element(*self._USERNAME).clear()
        self.driver.find_element(*self._PASSWORD).clear()

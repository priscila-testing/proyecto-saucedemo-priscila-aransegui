from selenium.webdriver.common.by import By
import time

def login(driver):
    driver.get("https://www.saucedemo.com/")  # # Navegar a la página de login

    driver.find_element(By.ID, "user-name").send_keys("standard_user")  # # Ingresar usuario válido
    driver.find_element(By.ID, "password").send_keys("secret_sauce")     # # Ingresar contraseña válida

    driver.find_element(By.ID, "login-button").click()  # # Click en login
    time.sleep(2)  # (Opcional, pausa corta)

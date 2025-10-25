from selenium.webdriver.common.by import By
import time

def login(driver):
    # # Navegar a la página de login
    driver.get("https://www.saucedemo.com/") 

    # # Ingresar usuario válido
    driver.find_element(By.ID, "user-name").send_keys("standard_user") 

    # # Ingresar contraseña válida
    driver.find_element(By.ID, "password").send_keys("secret_sauce")    
    
    # # Click en login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # (Opcional, pausa corta)

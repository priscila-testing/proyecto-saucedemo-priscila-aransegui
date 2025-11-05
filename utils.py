from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, timeout=15):
    # # Navegar a la página de login
    driver.get("https://www.saucedemo.com/") 

    # # Ingresar usuario válido
    driver.find_element(By.ID, "user-name").send_keys("standard_user") 

    # # Ingresar contraseña válida
    driver.find_element(By.ID, "password").send_keys("secret_sauce")    
    
    # # Click en login
    driver.find_element(By.ID, "login-button").click()
    
    # ESPERA EXPLÍCITA: que aparezcan los productos
    WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    time.sleep(1)
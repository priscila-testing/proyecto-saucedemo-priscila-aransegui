from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(login_in_driver):
    driver = login_in_driver

    # # Validar login exitoso con espera explícita
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_list")))  

    # # Validación URL
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    # # Validación texto Products
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "No se mostró el título 'Products'"  
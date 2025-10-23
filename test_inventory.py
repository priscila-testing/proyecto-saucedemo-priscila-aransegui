from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        assert driver.title == "Swag Labs"     # Verificar que el titulo de la página de inventario sea correcto

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos en la lista"
    
    except Exception as e:
        raise
    finally:
        driver.quit()
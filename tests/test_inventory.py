from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_inventory(login_in_driver):
    driver = login_in_driver

    # # Verificar que el titulo de la página de inventario sea correcto
    assert driver.title == "Swag Labs"     

    # # Verificar que haya productos visibles
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
        )
    assert len(products) > 0, "No hay productos en la lista"

    # # Verificar nombre y precio del primer producto
    first_product = products[0]
    name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert name == "Sauce Labs Backpack", "No se mostró el nombre 'Sauce Labs Backpack'"
    assert price == "$29.99", "No se mostró el precio '$29.99'"

    # # Validar que el menú y el filtro estén presentes en la página
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filters = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "No se muestra el menú"
    assert filters.is_displayed(), "No se muestran los filtros"

    time.sleep(2)
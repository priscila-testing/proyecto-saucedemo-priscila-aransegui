from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_cart(login_in_driver):
    driver = login_in_driver

    # # Añadir un producto al carrito
    add_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button")))
    add_button.click()
    # Guardar el nombre del producto agregado (opcional)
    title_product = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text

    # # Verificar que el contador del carrito se actualizó a 1
    cart_counter = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))).text
    assert cart_counter == "1", "No se ha agregado el producto al carrito"

    # # Hacer clic en el ícono del carrito / ir al carrito de compras
    cart_icon = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    # # Comprobar que el producto esté en el carrito
    cart_product_title = driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_name").text
    # Comprobar que el nombre coincide
    assert title_product == cart_product_title, "El producto no coincide"

    
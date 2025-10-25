from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_add_to_cart(login_in_driver):
    driver = login_in_driver

    # # Añadir un producto al carrito
    add_product = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_product.click()

    # # Verificar que el contador del carrito se actualizó
    cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1", "El contador del carrito no se incrementó"

    # # Navegar al carrito de compras
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    # # Comprobar que el producto esté en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert cart_item.text == "Sauce Labs Backpack", "El producto no aparece en el carrito"
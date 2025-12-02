from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    _INVENTORY_TITLE = (By.CLASS_NAME, "title")
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    # Elementos de interfaz/UI

    _MENU = (By.ID, "react-burger-menu-btn")
    _FILTRO = (By.CLASS_NAME, "product_sort_container")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def obtener_titulo_inventario(self):
        return self.driver.find_element(*self._INVENTORY_TITLE)

    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        return self.driver.find_elements(*self._INVENTORY_ITEMS)

    def obtener_nombre_producto(self):
        elems = self.wait.until(EC.visibility_of_all_elements_located(self._ITEM_NAME))
        return [e.text for e in elems]

    def obtener_precio_producto(self):
        elems = self.wait.until(EC.visibility_of_all_elements_located(self._ITEM_PRICE))
        return [e.text for e in elems]

    def verificar_menu_hamburguesa_visible(self):
        self.wait.until(EC.visibility_of_element_located(self._MENU))

    def verificar_filtro_visible(self):
        self.wait.until(EC.visibility_of_element_located(self._FILTRO))

    def verificar_boton_carrito_visible(self):
        self.wait.until(EC.visibility_of_element_located(self._CART_LINK))
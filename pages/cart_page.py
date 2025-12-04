from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_COUNTER = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def verificar_carrito_esta_vacio(self):
        contador = self.wait.until(EC.visibility_of_element_located(self._CART_LINK))
        texto = contador.text.strip()
        if texto == "":
            return 0
        return int(texto)

    def obtener_nombre_producto(self,index=0):
        nombres = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEM_NAME))
        return nombres[index].text

    def adicionar_producto_al_carrito(self, index=0):
        botones = self.wait.until(EC.visibility_of_all_elements_located(self._ADD_TO_CART_BUTTON))
        botones[index].click()        

    def obtener_conteo_carrito(self):
        try:
            contador = self.wait.until(EC.visibility_of_element_located(self._CART_COUNTER))
            return int(contador.text)
        except:
            return 0

    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()
        return self

    # Retorna una lista de nombres
    def obtener_todos_los_nombres(self):
        elems = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEM_NAME))
        return [e.text for e in elems]
    
    # Retorna una lista de elementos WebElement, no textos
    def obtener_productos_carrito(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return productos
    
    def agregar_producto_por_nombre(self,nombre_producto):
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)   

        for producto in productos:
            nombre = producto.find_element(*self._CART_ITEM_NAME).text

            if nombre.strip() == nombre_producto.strip():
                boton = producto.find_element(*self._ADD_TO_CART_BUTTON)
                boton.click()
                return self
        
    # Retorna solamente un nombre
    def obtener_nombre_producto_carrito(self):
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME))
        return nombre_producto.text
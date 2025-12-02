import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_csv_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login())
def test_navegacion_y_catalogo(login_in_driver, usuario, password, debe_funcionar):
    if not debe_funcionar:
        return  # Ignora usuarios que no deberían loguear

    driver = login_in_driver

    # Login
    login_page = LoginPage(driver)
    login_page.login_completo(usuario, password)

    inventory = InventoryPage(driver)

    # 1. Verificar título de la página de inventario
    titulo = inventory.obtener_titulo_inventario()
    assert titulo.is_displayed(), "El título 'Products' no está visible"
    assert titulo.text == "Products"

    # 2. Comprobar que existan productos visibles
    productos = inventory.obtener_todos_los_productos()
    assert len(productos) > 0, "No hay productos visibles en la página"

    # 3. Validar elementos importantes de la UI (menú, filtro, carrito)
    inventory.verificar_menu_hamburguesa_visible()
    inventory.verificar_filtro_visible()
    inventory.verificar_boton_carrito_visible()

    # 5. Listar nombre y precio del primer producto
    nombre = inventory.obtener_nombre_producto()
    precios = inventory.obtener_precio_producto()
    print(f"Nombre: {nombre[0]}, precio {precios[0]}")

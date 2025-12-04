import pytest
from pages.inventory_page import InventoryPage
import time

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    
    driver = login_in_driver
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
    time.sleep(2)

    # 4. Listar nombre y precio del primer producto
    nombre = inventory.obtener_nombre_producto()
    precios = inventory.obtener_precio_producto()
    print(f"Nombre: {nombre[0]}, precio {precios[0]}")
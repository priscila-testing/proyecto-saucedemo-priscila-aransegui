import pytest
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos

import time
RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    driver = login_in_driver
    cart_json = CartPage(driver)

    # Agregar al carrito el producto
    cart_json.agregar_producto_por_nombre(nombre_producto)

    # Abrir el carrito
    cart_json.abrir_carrito()
    time.sleep(1)

    # Validar el producto
    assert cart_json.obtener_nombre_producto_carrito() == nombre_producto
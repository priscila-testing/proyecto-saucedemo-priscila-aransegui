import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.datos import leer_csv_login
from utils.lector_json import leer_jason_productos
import time

RUTA_JASON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login())
@pytest.mark.parametrize("nombre_producto", leer_jason_productos(RUTA_JASON))
def test_carrito_json(login_in_driver, usuario, password, debe_funcionar, nombre_producto):
    if not debe_funcionar:
        return

    driver = login_in_driver

    login_page = LoginPage(driver)
    login_page.login_completo(usuario, password)

    cart = CartPage(driver)

    # Obtener nombre real del producto que voy a agregar
    nombre_esperado = cart.obtener_nombre_producto(0)

    # 1. Adicionar el primer producto al carrito
    cart.adicionar_producto_al_carrito(0)
    time.sleep(2)

    # 2. Verificar que el contador sea 1
    assert cart.obtener_conteo_carrito() == 1
    time.sleep(1)

    # 3. Abrir carrito de compras
    cart.abrir_carrito()

    # 4. Verificar productos en el carrito
    en_carrito = cart.obtener_todos_los_nombres()
    time.sleep(3)

    # Verificar que solo haya 1 producto
    assert len(en_carrito) == 1
    
    # Verificar que sea el mismo que agregaste
    assert en_carrito[0] == nombre_esperado
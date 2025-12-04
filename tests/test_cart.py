import pytest
from pages.cart_page import CartPage
import time

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):

    driver = login_in_driver
    cart = CartPage(driver)

    # Verificar que el carrito está vacío al início
    assert cart.verificar_carrito_esta_vacio() == 0
    time.sleep(1)

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
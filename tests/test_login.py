import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login
import time

@pytest.mark.parametrize("usuario,password,debe_funcionar", leer_csv_login())
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    driver = login_in_driver
    login = LoginPage(driver)

    # 1. Navegar a la pagina de login
    login.abrir_pagina()       

    # 2. Ingresar usuario y contraseña desde CSV             
    login.login_completo(usuario, password) 

    if debe_funcionar:
        # 3. Validar login exitoso y verificar que se redirigió a la pagina de inventario
        assert "/inventory.html" in driver.current_url
        time.sleep(3)

        # 4. Verificar que el logo "Swag Labs" sea visible
        logo = login.obtener_logo_pagina()
        assert logo.is_displayed(), "El logo 'Swag Labs' no está visible"
        time.sleep(3)

    else:
        # Validar login fallido
        mensaje_error = login.obtener_error()
        assert mensaje_error != "", "No se mostró ningún mensaje de error"

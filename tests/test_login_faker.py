import pytest
from pages.login_page import LoginPage
# Importamos
from faker import Faker

# Inicializamos
faker = Faker()

@pytest.mark.parametrize("usuario,password,debe_funcionar", [
    (faker.user_name(),faker.password(length=8,special_chars=True,upper_case=True,lower_case=True,digits=True),False),
    (faker.user_name(),faker.password(),False)
])
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    driver = login_in_driver
    login = LoginPage(driver)

    login.abrir_pagina()       

    login.login_completo(usuario, password) 

    if debe_funcionar:

        assert "/inventory.html" in driver.current_url

        logo = login.obtener_logo_pagina()
        assert logo.is_displayed(), "El logo 'Swag Labs' no está visible"

    else:
        mensaje_error = login.obtener_error()
        assert mensaje_error != "", "No se mostró ningún mensaje de error"

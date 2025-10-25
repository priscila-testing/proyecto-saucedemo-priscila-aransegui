import pytest
from selenium import webdriver
from utils import login

# # Inicializamos el navegador Chome
@pytest.fixture
def browser_driver():
    driver = webdriver.Chrome()    # Abre el navegador Chrome
    yield driver                   # Entrega el navegador al test para que lo use
    driver.quit()                  # Cierra el navegador al final del test

# # Login en la página web antes de cada test
@pytest.fixture
def login_in_driver(browser_driver):
    login(browser_driver)              # Hace login en el navegador
    return browser_driver              # Devulve el navegador abierto y logueado
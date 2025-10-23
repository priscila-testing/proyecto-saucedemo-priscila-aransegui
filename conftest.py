import pytest
from selenium import webdriver
from utils import login

# Inicializamos todo lo que es el navegador
@pytest.fixture
def driver():
    driver = webdriver.Chrome()    # Abre el navegador
    yield driver                   # Entrega el navegador al test
    driver.quit()                  # Cierra el navegador al final del test

@pytest.fixture
def login_in_driver(driver):
    login(driver)  # # Login antes del test
    return driver
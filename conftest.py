import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

import time

# # Inicializamos el navegador Chrome
@pytest.fixture(scope="session")
def browser_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver                   # Entrega el navegador al test para que lo use
    driver.quit()                  # Cierra el navegador al final del test

# # Login en la página web antes de cada test
@pytest.fixture(scope="session")
def login_in_driver(browser_driver):
    LoginPage(browser_driver).abrir_pagina()
    time.sleep(2)
    return browser_driver          # Devuelve el navegador abierto y logueado
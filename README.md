# proyecto-saucedemo-priscila-aransegui
Proyecto de automatización de pruebas en SauceDemo usando Python, Selenium, Pytest y Git.

Introducción:
En este proyecto estudié y practiqué la automatización de pruebas funcionales sobre la página SauceDemo, una tienda de demostración diseñada para ejercicios de testing.
El objetivo principal fue aprender a crear pruebas automáticas usando Python, Selenium y Pytest, verificando desde el login hasta el carrito de compras. Además, utilicé Git para versionar el código y GitHub para almacenar el proyecto como parte de mi portafolio, mostrando de manera profesional los avances y cambios realizados durante el estudio.
Dividí la explicación del proyecto en seis partes principales, que se detallan a continuación en el cuerpo del documento.
I.	Primero, creé un archivo llamado utils.py en la raíz del proyecto.
Ese archivo sirve para guardar funciones que voy a usar varias veces.
Creé una función llamada login con un parámetro driver. Ese parámetro es el WebDriver de Selenium, que controla el navegador que me entrega Pytest.
Pasé el parámetro driver como argumento para que la función login sepa sobre qué navegador actuar (en este momento driver es solo un hueco que la función llenará cuando reciba un navegador real creado más adelante en otro archivo). Así, puedo reutilizar la función en cualquier test sin tener que crear un nuevo navegador dentro de utils.py
Dentro de la función login, utilicé get junto a driver para abrir la página web y find_element para buscar los campos de usuario, contraseña y el botón de envío de datos usando By para buscar el id del elemento. Luego, llamé al método click() sobre el botón, que sirve para simular un clic del usuario y enviar los datos del formulario.
Agregué un timer para hacer una pausa corta en el test de la página (ver comentario más abajo).
En utils.py, además importé:
from selenium.webdriver.common.by import By para decir a Selenium cómo buscar los elementos en la página.
import time lo usé para hacer pausas pequeñas mientras Selenium espera que la página cargue los elementos (con time.sleep()). 

II.	Segundo, creé un archivo llamado conftest.py en la raíz del proyecto.
En ese archivo se definen configuraciones y fixtures que se van a compartir entre varios archivos de test.
Importé de utils.py la función login (ver comentario más abajo).
a) Creé una función llamada browser_driver (sin parámetro) para definir el navegador que voy a usar.
Dentro de esa función, creé una variable llamada driver y utilicé el webdriver de Selenium para definir el navegador como “Chrome”.
Devolví el navegador al test con yield.
Luego, llamé nuevamente el driver de utils.py y, junto a él, utilicé quit() para cerrar completamente el navegador al terminar la sesión de Selenium en cada test. Luego comenté esa línea para que el navegador no abre y cierre varias veces.
Marqué la función con el decorador @pytest.fixture(scope="session") para que Pytest pueda reutilizarla en varios tests y abrir el navegador una sola vez.
b) Creé una @pytest.fixture, que sirve para preparar el navegador ya logueado y hacer el login.
Definí el nombre de la función como login_in_driver y le pasé como parámetro la fixture anterior (browser_drive), para llamar el mismo navegador Chrome y utilizarlo.
Dentro de la función, ejecuté la función login de utils.py para hacer login real dentro del navegador.
Con el return pasé al test el navegador preparado, listo para interactuar con la página.
En conftest.py importé:
import pytest para crear y manejar los tests y los fixtures
from selenium import webdriver para abrir y controlar el navegador que vamos a usar en los tests
from utils import login para poder usar la función de login dentro de los fixtures
III.	En tercero lugar, creé un archivo llamado test_login.py en la raíz del proyecto.
En ese archivo valido el login exitoso usando espera explícita, verificando que la URL después del login sea correcta y que el texto “Products” esté visible en la página.
Creé una función llamada test_login_success y le pasé como parámetro la fixture login_in_drive de conftest.py, para hacer login en la página, porque esa fixture devuelve el navegador Chrome ya abierto y logueado.
Dentro de la función, creé una variable local llamada driver para guardar el navegador; a partir de ahí, todo lo que haga con driver ya estará logueado en la página.
Utilicé WebDriverWait con una pausa explícita de 10 segundos para validar que los elementos del inventario estén presentes. Para eso, utilicé el nombre de la clase del inventario y la busqué con By.
Con assert, verifiqué si la condición es verdadera para confirmar que la página se redirigió al URL "/inventory_list.html". 
Usé assert para verificar que el texto del título sea “Products”'; primero encontré el elemento con find_element usando su clase (a través de By) y luego obtuve el texto visible en pantalla con el atributo text.
Pare que sea posible hacer estos tests, en test_login.py importé:
from selenium.webdriver.common.by import By otra vez.
from selenium.webdriver.support.ui import WebDriverWait para esperar un tiempo determinado hasta que un elemento esté presente o cumpla cierta condición, evitando errores si la página tarda en cargar.
from selenium.webdriver.support import expected_conditions as EC para traer condición predefinida “elemento visible” que usé junto a WebDriverWait.

IV.	En cuarto lugar, creé un archivo llamado test_inventory.py en la raíz del proyecto.
En ese archivo verifico que el título de la página de inventario sea correcto, que haya productos visibles, compruebo nombre y precio del primer producto, y valido que los elementos importantes de la interfaz, menú y filtros, estén presentes.
Creé una función llamada test_inventory y le pasé como parámetro la fixture login_in_drive de conftest.py, para hacer login en la página.
Dentro de la función, guardé el navegador en una variable local llamada driver para poder usarlo directamente.
En assert, usé el driver con el atributo title y verifiqué que el título de la página abierta en el navegador sea exactamente “Swag Labs”.
Creé una variable llamada products y en ella usé el driver con find_elements para obtener todos los productos de la página a través de By con su clase. Utilicé WebDriverWait con una espera explícita para que Selenium espere hasta que los elementos de la página estén presentes o visibles antes de interactuar con ellos. Esto asegura que el test no falle si la página tarda en cargar los productos o botones, haciendo la automatización más confiable.
Con assert y la función len usando como parámetro la variable products, verifiqué que la cantidad de elementos encontrados en la página fuera mayor a cero.
Creé una variable llamada first_product con el primer producto de la lista, y en ella usé find_element con By por clase para obtener su nombre en “name” y su precio en “price”.
Usé assert para verificar que el nombre del primer producto sea “Sauce Labs Backpack” y que su precio sea “$29.99”.
Por último, en la misma función, creé una variable llamada menu y en ella usé el driver con find_elements para obtener el elemento a través de By por su id.
Luego creé una variable llamada filters y en ella usé el driver con find_element para obtener el elemento a través de By por su clase.
Con assert verifiqué el resultado del método is_displayed() de Selenium para confirmar que los elementos “menú” y el elemento “filtro” estén visibles en la página.
En test_inventory.py importé:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



V.	En quinto lugar, creé un archivo llamado test_cart.py en la raíz del proyecto.
En ese archivo agrego un producto al carrito, verifico que el contador del carrito se incremente, navego al carrito de compras y compruebo que el producto aparezca correctamente.
Creé una función llamada test_add_to_cart que recibe como parámetro la fixture login_in_drive de conftest.py, para trabajar con un navegador ya logueado.
Dentro de la función, guardé el navegador en una variable local llamada driver para poder usarlo directamente.
Creé una variable llamada add_product y utilicé find_element junto con By para buscar el botón por su id. Luego, llamé al método click() sobre esa variable para simular un clic y añadir un producto al carrito.
Creé una variable llamada cart_badge y utilicé WebDriverWait con una espera explícita para que Selenium espere hasta que el contador del carrito, buscado por su clase con By, sea visible. Luego, con assert verifiqué que el texto visible del contador, obtenido con el atributo text, se hubiera actualizado a “1”.
Creé una variable llamada cart_icon y utilicé find_element junto con By para buscar el ícono del carrito por su clase. Luego, llamé al método click() sobre esa variable para navegar al carrito de compras.
Creé una variable llamada cart_item y utilicé find_element junto con By para buscar el nombre del producto en el carrito por su clase. Luego, con assert verifiqué que el texto visible en pantalla, obtenido con el atributo text, fuera “Sauce Labs Backpack”.
En test_cart.py importé:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

VI.	En sexto lugar, creé un archivo llamado run_tests.py en la raíz del proyecto.
En ese archivo defino la lista de archivos de prueba que se ejecutarán, con el objetivo de centralizar la ejecución de todas las pruebas desde un único archivo, evitando la necesidad de ejecutarlas desde los otros archivos de prueba.
Para ello, creé una carpeta nueva llamada tests dentro de la carpeta del proyecto (proyecto-saucedemo-priscila-aransegui) y moví allí los tres archivos de test.
En run_tests.py escribí una lista llamada test_files que contiene una lista con los nombres de esos tres tests.
Luego, creé una variable llamada pytest_args y le asigné el valor de test_files sumando otra lista con los argumentos para ejecutar las pruebas y generar un reporte. El reporte sirve para ver de manera ordenada y detallada cuáles tests pasaron, cuáles fallaron y qué errores ocurrieron, incluyendo información visual si usamos HTML.
Para generar el reporte utilicé los argumentos --html=report.html, --self-contained-html y -v, que indican respectivamente el nombre del archivo de reporte, que el reporte incluya todo en un solo archivo y que la salida sea más detallada.
Al final, llamé a pytest.main pasando cómo parámetro la variable pytest_args; esto ejecuta todos los tests indicados en la lista junto con los argumentos que definí.
Así puedo correr todos los tests de forma centralizada desde run_tests.py y obtener automáticamente el reporte sin tener que ejecutar cada test individualmente.
En run_tests.py importé:
import pytest

Conclusión
Este proyecto me permitió practicar y consolidar conocimientos en automatización de pruebas, desde la interacción con elementos web hasta la organización de tests y generación de reportes. Además, la integración de Git y GitHub permitió versionar y almacenar el proyecto como parte de mi portafolio, mostrando de forma clara mi progreso y habilidades en testing automatizado. SauceDemo sirvió como entorno seguro para experimentar sin afectar aplicaciones reales.

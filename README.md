PORTAFOLIO – Proyecto de Automatización

Tecnologías utilizadas: Python, Selenium, Pytest, Git y GitHub
Autora: Priscila Menezes Aransegui
Repositorio GitHub: https://github.com/priscila-testing/proyecto-saucedemo-priscila-aransegui.git

Introducción

En este proyecto estudié y practiqué la automatización de pruebas funcionales sobre la página SauceDemo, una tienda de demostración diseñada para ejercicios de testing.
El objetivo principal fue aprender a crear pruebas automáticas usando Python, Selenium y Pytest, verificando desde el login hasta el carrito de compras. Además, utilicé Git para versionar el código y GitHub para almacenar el proyecto como parte de mi portafolio, mostrando de manera profesional los avances y cambios realizados durante el estudio.

📘 El proyecto incluye

•	Tests automatizados con Selenium y Pytest.
•	Fixtures reutilizables para login y control del navegador.
•	Validaciones funcionales de login, inventario y carrito.
•	Uso de esperas explícitas (WebDriverWait + expected_conditions) para hacer los tests más confiables.
•	Estructura organizada para facilitar mantenimiento y escalabilidad.


⚙️ Requisitos prévios

•	Python 3.10 o superior.
•	Google Chrome instalado.
•	Selenium.
•	WebDriver (Chromedriver).
•	Bibliotecas necesarias: pip install selenium pytest pytest-html
•	Git y GitHub (para control de versiones y publicación del proyecto).


Dividí la explicación del proyecto en seis partes principales, que se detallan a continuación en el cuerpo del documento.


🔹 Desarrollo del proyecto

1. utils.py

•	Archivo de funciones reutilizables.
•	Función login(driver) que recibe el WebDriver y realiza el login en SauceDemo.
•	Busca campos de usuario, contraseña y botón de envío.
•	Simula clic y envío de datos.
•	Incluye pausas con time.sleep() para cargar elementos.


2. conftest.py

•	Define fixtures compartidas entre tests:
•	browser_driver: crea y devuelve un navegador Chrome. Decorada con @pytest.fixture(scope="session") para abrir el navegador solo una vez por sesión.
•	login_in_driver: llama a browser_driver y ejecuta login(driver), devolviendo un navegador ya logueado.
•	Librerías importadas: pytest, webdriver, login de utils.


3. test_login.py

•	Testea el login exitoso.
•	Fixture usada: login_in_driver.
•	Validaciones: URL de redirección correcta y título de página “Products” visible.
•	Uso de esperas explícitas para evitar fallos por carga lenta.


4. test_inventory.py

•	Verifica inventario y elementos de la interfaz.
•	Validaciones:
•	Título de la página “Swag Labs”.
•	Presencia de productos (.inventory_item).
•	Nombre y precio del primer producto.
•	Visibilidad de menú y filtros.
•	Uso de esperas explícitas y assert para validar contenido.


5. test_cart.py

•	Añade productos al carrito y verifica su correcto agregado.
•	Flujo:
•	Clic en botón del primer producto (.inventory_item button).
•	Guardar nombre del producto en title_product.
•	Espera explícita para contador del carrito (.shopping_cart_badge).
•	Clic en ícono del carrito (.shopping_cart_link).
•	Comparar nombre del producto en carrito con title_product.


6. run_tests.py

•	Archivo central para ejecutar todos los tests y generar reportes.
•	Lista de tests dentro de test_files.
•	Argumentos de Pytest: --html=report.html --self-contained-html -v para generar reporte HTML detallado.


Conclusión

Este proyecto me permitió practicar y consolidar conocimientos en automatización de pruebas, desde la interacción con elementos web hasta la organización de tests y generación de reportes. Además, la integración de Git y GitHub permitió versionar y almacenar el proyecto como parte de mi portafolio, mostrando de forma clara mi progreso y habilidades en testing automatizado. SauceDemo sirvió como entorno seguro para experimentar sin afectar aplicaciones reales.


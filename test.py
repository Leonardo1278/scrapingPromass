# Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import logging
import time
import csv

#%% CONFIGURACIÓN DEL LOGGER
logger = logging.getLogger('myAppLogger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

#%% OPCIONES DE CHROME
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("start-maximized")
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('useAutomationExtension', False)

coches = (
    'PORSCHE 911 CARRERA 4S',
    'POLO JOIN TIP 1.6L  4CIL',
    'POLO STARLINE STD 1.6L 4CIL',
    'POLO STARLINE TIP 1.6L 4CIL',
    'PORSCHE 911 CARRERA 4S',
    'PORSCHE 911 TURBO S COUPE',
    'PORSCHE CAYENNE S COUPE AUT',
    'PRIUS BASE HIBRIDO CVT 1.8L 4CIL',
    'PRIUS HEV PREMIUM AUT 1.8L 4CIL',
    'PRIUS PREMIUM AUT HIBRIDO 1.8L 4CIL',
    'PULSE IMPETUS AUT  4 CIL 1.3L',
    'Q2 DYNAMIC 35 TFSI 1.4 AUT',
    'Q2 SELECT 35 TFSI 1.4 AUT',
    'Q2 SPORT 35 TFSI 1.4 AUT'
)

coches = (
    'PORSCHE 911 CARRERA 4S',
    'POLO JOIN TIP 1.6L  4CIL',
    'Q2 SPORT 35 TFSI 1.4 AUT'
)

s = Service(r'chromedriver.exe')

#%% URL
url = 'https://www.autocompara.com/?gad_source=1&gbraid=0AAAAAC2MRaVSJdzIzyof1NTRZ9k9bfGZ-&gclid=EAIaIQobChMI9_iRy5_yjAMVDChECB3HfB8VEAAYASAAEgKoHfD_BwE&gclsrc=aw.ds'

#%% INICIAR DRIVER
driver = webdriver.Chrome(service=s, options=options)
driver.get(url)
# Lista para almacenar todos los datos
datos_cards = []
for coche in coches: 
    #%% INGRESAR AÑO
    año = "2022"
    input_button_xpath = '//*[@id="year"]'

    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, input_button_xpath))
    )
    input_element.clear()
    time.sleep(0.5)
    input_element.send_keys(año)
    logger.info(f"Año ingresado: {año}")
    time.sleep(2)

    #%% SELECCIONAR MODELO (usando variable `coche`)
    ng_select_xpath = '//*[@id="search"]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ng_select_xpath)))
    ng_select = driver.find_element(By.XPATH, ng_select_xpath)
    ng_select.click()
    logger.info("Desplegable de modelo abierto")

    # Ingresar texto del modelo (de la variable `coche`)
    input_modelo_xpath = ng_select_xpath + '/div/div/div[2]/input'
    input_modelo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, input_modelo_xpath)))
    input_modelo.clear()
    input_modelo.send_keys(coche)
    time.sleep(2)  # Espera a que aparezcan resultados

    # Seleccionar la primera coincidencia después de escribir el modelo
    options_xpath = '//div[contains(@class, "ng-option-child")]'
    primera_opcion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'({options_xpath})[1]'))
    )
    modelo = primera_opcion.text
    primera_opcion.click()
    logger.info(f"Modelo seleccionado: {modelo}")

    #%% CONTINUAR
    time.sleep(2)
    continuar_path = "/html/body/app-root/block-ui/div/div/ac-home/section/div[2]/div[1]/div[2]/ac-vehicle-data-home/section/div/div[3]/div[6]/div[2]/button"

    continuar_boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, continuar_path))
    )
    continuar_boton.click()
    logger.info("Se hizo clic en el botón de continuar")

    time.sleep(2)

    # Esperar y hacer clic en el label deseado después del botón continuar
    label_xpath = "/html/body/app-root/block-ui/div/div/ac-home/section/div[2]/div[1]/div[2]/ac-vehicle-data-home/section/div/ac-quotation-data-home/section/form/div/div[2]/div[1]/div/label[1]"

    label_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, label_xpath))
    )
    label_element.click()
    logger.info("Se hizo clic en el label [1] después de continuar")
    time.sleep(1)

    # Ingresar la fecha 15/02/2000
    fecha_xpath = '//*[@id="date"]'
    fecha = '15/02/2000'

    fecha_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, fecha_xpath))
    )
    fecha_input.clear()
    fecha_input.send_keys(fecha)
    logger.info(f"Fecha ingresada: {fecha}")
    #time.sleep(1)

    # Ingresar el nombre "Leonardo Daniel"
    nombre_xpath = '//*[@id="name"]'
    nombre = 'Leonardo Daniel'

    nombre_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, nombre_xpath))
    )
    nombre_input.clear()
    nombre_input.send_keys(nombre)
    logger.info(f"Nombre ingresado: {nombre}")
    #time.sleep(1)

    # Ingresar el código postal 07700
    cp_xpath = '//*[@id="cp"]'
    codigo_postal = '07700'

    cp_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, cp_xpath))
    )
    cp_input.clear()
    cp_input.send_keys(codigo_postal)
    logger.info(f"Código postal ingresado: {codigo_postal}")
    #time.sleep(1)

    # Ingresar el correo electrónico ldcuetoc@gmail.com
    correo_xpath = '//*[@id="email"]'
    correo = 'ldcuetoc@gmail.com'

    correo_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, correo_xpath))
    )
    correo_input.clear()
    correo_input.send_keys(correo)
    logger.info(f"Correo ingresado: {correo}")
    #time.sleep(1)

    # Ingresar el número telefónico 5585378966
    telefono_xpath = '//*[@id="phone"]'
    telefono = '5585378966'

    telefono_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, telefono_xpath))
    )
    telefono_input.clear()
    telefono_input.send_keys(telefono)
    logger.info(f"Teléfono ingresado: {telefono}")
    #time.sleep(1)

    # Hacer clic en el botón para obtener cotizaciones
    cotizar_btn_xpath = '/html/body/app-root/block-ui/div/div/ac-home/section/div[2]/div[1]/div[2]/ac-vehicle-data-home/section/div/ac-quotation-data-home/section/div/div[3]/button'
    cotizar_boton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, cotizar_btn_xpath))
    )
    # Espera extra por si hay overlays o spinners
    time.sleep(2)
    # Forzar el clic con JavaScript para evitar overlays
    driver.execute_script("arguments[0].click();", cotizar_boton)
    logger.info("Se hizo clic (forzado) en el botón de obtener cotizaciones")
    logger.info("Se hizo clic en el botón de obtener cotizaciones")
    time.sleep(5)



    try:    #%% ESPERAR A QUE APAREZCAN LAS CARDS DE COTIZACIÓN
        cards_xpath = '//div[@class="cards"]'  # Asegúrate de ajustar esta clase al HTML real
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, cards_xpath))
        )

        # Obtener todas las cards
        cards = driver.find_elements(By.XPATH, cards_xpath)

        logger.info(f"Se encontraron {len(cards)} tarjetas de cotización")

            # Iterar y extraer texto de cada card
        for idx, card in enumerate(cards, start=1):
            try:
                contenido = card.text  # .text trae todo el contenido visible de la tarjeta
                logger.info(f"Contenido de la tarjeta {idx}:\n{contenido}\n{'-'*40}")
            except Exception as e:
                logger.error(f"No se pudo extraer la tarjeta {idx}: {e}")
        time.sleep(1)

    except Exception as e:
            logger.warning(f"No hay cotizaciones disponibles {e}")
            driver.get(url)
            continue

    # Ruta para guardar el archivo CSV
    output_file = 'cotizaciones.csv'



    # XPaths de botones de cobertura
    coberturas = {
        "Amplia": None,  # Ya está activa por defecto
        "Limitada": '/html/body/app-root/block-ui/div/div/ac-quotation/section/div[4]/div[1]/div/div[2]/div[2]/label[2]',
        "RC": '/html/body/app-root/block-ui/div/div/ac-quotation/section/div[4]/div[1]/div/div[2]/div[2]/label[3]',
    }

    # Iterar por cada tipo de cobertura
    for tipo_cobertura, xpath in coberturas.items():
        if xpath:
            try:
                btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].click();", btn)
                logger.info(f"🔁 Cambiada a cobertura: {tipo_cobertura}")
                time.sleep(5)  # Espera que se actualicen las cards
            except Exception as e:
                logger.warning(f"No se pudo cambiar a cobertura {tipo_cobertura}: {e}")
                continue
        else:
            logger.info(f"Procesando cobertura inicial: {tipo_cobertura}")

        # Esperar las cards
        cards_xpath = '//div[@class="cards"]'
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, cards_xpath)))
        cards = driver.find_elements(By.XPATH, cards_xpath)
        logger.info(f"{len(cards)} tarjetas encontradas para cobertura {tipo_cobertura}")

        # Iterar y extraer texto de cada card
        for idx, card in enumerate(cards, start=1):
            try:
                contenido = card.text.strip().split("\n")
                logger.info(f"Contenido de la tarjeta {idx} ({tipo_cobertura}):\n{contenido}\n{'-'*40}")

                # Inicializar datos base
                etiqueta = ""
                precio_anual = ""
                precio_anual_desc = ""
                mensualidad = ""
                mensualidad_desc = ""

                # Asignar valores dinámicamente según el contenido
                for i, line in enumerate(contenido):
                    if "barato" in line.lower():
                        etiqueta = line
                    if "Pago anual" in line:
                        if i + 2 < len(contenido):
                            precio_anual = contenido[i + 1]
                            precio_anual_desc = contenido[i + 2]
                        elif i + 1 < len(contenido):
                            precio_anual = contenido[i + 1]
                    if "MSI" in line:
                        if i + 2 < len(contenido):
                            mensualidad = contenido[i + 1]
                            mensualidad_desc = contenido[i + 2]
                        elif i + 1 < len(contenido):
                            mensualidad = contenido[i + 1]

                # Agregar al listado final
                datos_cards.append({
                    "Modelo": modelo,
                    "Año": año,
                    "Tipo de cobertura": tipo_cobertura,
                    "Etiqueta": etiqueta,
                    "Precio anual": precio_anual,
                    "Precio con descuento": precio_anual_desc,
                    "Mensualidad": mensualidad,
                    "Mensualidad con descuento": mensualidad_desc
                })

            except Exception as e:
                logger.error(f"No se pudo extraer info de la tarjeta {idx} para cobertura {tipo_cobertura}: {e}")

    driver.get(url)
    time.sleep(5)

# Escribir los datos en un archivo CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=datos_cards[0].keys())
    writer.writeheader()
    writer.writerows(datos_cards)

logger.info(f"Archivo CSV guardado: {output_file}")
print(f"Archivo CSV guardado exitosamente en: {output_file}")
time.sleep(10)

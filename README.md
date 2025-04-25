![image](https://github.com/user-attachments/assets/2d07484e-881d-4345-860a-e96c29b3902b)


# 🚗 Scraper de Cotizaciones – Autocompara

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-success)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-orange)
![License](https://img.shields.io/badge/Licencia-MIT-lightgrey)

---

## 🧠 Resumen Ejecutivo

Se logró implementar exitosamente un proceso de scraping en el sitio **[Autocompara](https://www.autocompara.com)** (Angular 16.2.12) utilizando **Selenium**, después de intentar con otras tecnologías como:

- Puppeteer
- Playwright
- NgWebDriver
- BeautifulSoup
- ZenRows

🔒 Todas fueron bloqueadas por detección activa de bots. (Se pueden anexar los códigos usados si se requiere).

📊 Debido a la magnitud de combinaciones posibles (**+30,000 modelos**, múltiples años y coberturas), el scraping completo con navegador no es viable actualmente.

🖼 Además, los nombres de las aseguradoras vienen como **imágenes**, lo que obliga a aplicar técnicas de **reconocimiento óptico (OCR)** para poder extraer esa información y tener una base de datos funcional.

🔍 Se exploraron posibles endpoints/API ocultas del sitio, pero no exponen la información completa necesaria para obtener las cotizaciones.

> **Conclusión:** El problema requiere una revaloración técnica y más tiempo de desarrollo para alcanzar una solución escalable, eficiente y precisa.

---

## 🗂 Estructura del Proyecto

Esta carpeta está organizada para cubrir todo el ciclo: scraping → transformación → análisis.

### 📁 Archivos principales

| Archivo | Descripción |
|--------|-------------|
| `test.py` | Script principal en Python (Selenium) para obtener cotizaciones por modelo. |
| `chromedriver.exe` | Driver necesario para ejecutar Selenium con Google Chrome. |
| `cotizaciones.csv` | Salida con todas las cotizaciones obtenidas. Incluye coberturas, precios anuales y mensualidades. |
| `cookies_autocompara.txt` | (Opcional) Cookies de sesión para pruebas más avanzadas. |
| `etlResidentes.py` | Transforma archivos `.json` de cotizaciones en formato tabular (CSV). |
| `residentes.json` | Archivo JSON con cotizaciones para residentes. |
| `residentes.csv`, `ofertas_residentes.csv` | Archivos procesados a partir de `residentes.json`. |

### 📁 Archivos de entrada y catálogos

- `modelos_autocompara.csv`: Lista de modelos usados como input para scraping.
- `formas_pago_autocompara.csv`, `planes.csv`, `deducibles.csv`, `nacionalidades.csv`, `profesiones.csv`, `socios.csv`: Catálogos usados para simular distintas configuraciones.  
  > Generados como salida del script `index.js`.

### 📁 Scripts auxiliares (Node.js)

- `index.js`, `puppeteer_get_residentes.js`: Scripts alternativos usando **Puppeteer** para pruebas complementarias o generación de archivos base.

---

## ⚙️ Requisitos

- Python 3.10+
- Google Chrome
- Selenium
- ChromeDriver (misma versión que tu navegador)

Instalación de dependencias:
```bash
pip install selenium

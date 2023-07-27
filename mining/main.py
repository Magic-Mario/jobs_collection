# sourcery skip: use-contextlib-suppress
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.environ["PATH"] += r"C:/SeleniumDrivers"


def get_job(key_word: str, location: str = "Colombia", pag_count: int = 5):
    """
    Obtiene datos de ofertas de trabajo de Computrabajo para una palabra clave y ubicación específicas.

    Parámetros:
        - key_word (str): Palabra clave para la búsqueda de trabajo.
        - location (str, opcional): Ubicación para la búsqueda de trabajo. Por defecto es "Colombia".
        - pag_count (int, opcional): Número de páginas a obtener. Por defecto es 5.

    Retorna:
        Una lista de diccionarios con los datos de las ofertas de trabajo scrapeadas de Computrabajo.
    """
    scraped_data = []  # Inicializar una lista vacía para almacenar los datos scrapeados

    for page_num in range(start=1, stop=pag_count):
        url = f"https://co.computrabajo.com/trabajo-de-{key_word}-en-{location}?p={page_num}"
        browser.get(url)
        browser.implicitly_wait(30)
        app = browser.find_elements(By.CLASS_NAME, "box_offer")

        # Llamar a la función computrabajo_scraper para obtener datos de la página actual
        page_data = computrabajo_scraper(app)
        scraped_data.extend(
            page_data
        )  # Agregar los datos de la página actual a la lista general

    return scraped_data


def computrabajo_scraper(app: list):  # sourcery skip: use-contextlib-suppress
    """
    Obtiene datos de ofertas de trabajo de la página de Computrabajo.

    Parámetros:
        - app (list): Lista de elementos web que contienen información sobre las ofertas de trabajo.

    Retorna:
        Una lista de diccionarios con los datos de las ofertas de trabajo scrapeadas de la página.
    """
    scraped_data = []  # Inicializar una lista vacía para almacenar los datos scrapeados
    for item in app:
        title = item.find_element(By.TAG_NAME, "h2").text
        link_element = browser.find_element(By.CLASS_NAME, "js-o-link")
        href = link_element.get_attribute("href")

        company = None

        try:
            # Agregar tiempo de espera adicional antes de buscar el elemento
            browser.implicitly_wait(2)
            company = item.find_element(
                By.CSS_SELECTOR, "p.fs16.fc_base.mt5.mb5 a.fc_base"
            ).text
            location_item = item.find_element(
                By.CSS_SELECTOR, "p.fs16.fc_base.mt5.mb5"
            ).text.split()
            replace_cities = {"D.C.": "Bogotá", "Indias": "Cartagena"}
            location_output = [
                replace_cities.get(item, item) for item in location_item
            ][-1]
        except Exception:
            # Si no se encuentra el elemento, se deja como None
            pass

        # Agregar el diccionario de datos a la lista
        scraped_data.append(
            {
                "platform": "Computrabajo",
                "title": title,
                "company": company,
                "location": location_output,
                "link": href,
            }
        )

    return scraped_data  # Retornar la lista con todos los datos scrapeados


if __name__ == "__main__":
    browser = webdriver.Chrome()
    result = get_job(key_word="python")
    print(result)
    print(len(result))

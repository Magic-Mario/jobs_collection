# sourcery skip: use-contextlib-suppress
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.environ["PATH"] += r"C:/SeleniumDrivers"

browser = webdriver.Chrome()
browser.get("https://co.computrabajo.com/trabajo-de-python-en-barranquilla")
browser.implicitly_wait(30)
box_offer = browser.find_elements(By.CLASS_NAME, "box_offer")

for item in box_offer:
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
        location_output = [replace_cities.get(item, item) for item in location_item][-1]
    except Exception:
        # Si no se encuentra el elemento, se deja como None
        pass

    print(title)
    print(company)
    print(location_output)
    print(href)
    print("--------------")

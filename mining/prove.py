from selenium import webdriver
import os

os.environ['PATH'] += r"C:/SeleniumDrivers"


driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/JqueryProgressBar.html')
driver.implicitly_wait(30)
id_element = driver.find_element('id', 'downloadButton')
id_element.click()
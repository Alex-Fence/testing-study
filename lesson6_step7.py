# последовательно взять каждый элемент из найденного списка текстовых полей и отправить произвольный текст в каждое поле

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    #поместить все строки содержащие тег input в список
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        #заполнение всех полей заданным словом
        element.send_keys("Ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

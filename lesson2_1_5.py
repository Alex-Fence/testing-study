from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get(link)
x = browser.find_element(By.ID, 'input_value').text
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
browser.find_element(By.CLASS_NAME, 'btn-default').click()

# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

time.sleep(10)
browser.quit()

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get('http://suninjuly.github.io/selects2.html')
sum_numbs = int(browser.find_element(By.ID, 'num1').text)+int(browser.find_element(By.ID, 'num2').text)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum_numbs))
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)
browser.quit()

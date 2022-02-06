from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/math.html"
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
x = browser.find_element(By.ID,'input_value')

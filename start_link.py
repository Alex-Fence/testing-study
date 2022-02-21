from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def start(link):
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    return browser.get(link)

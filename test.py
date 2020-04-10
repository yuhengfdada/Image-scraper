from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import imageio

class imagebot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open(self):
        self.driver.get('https://www.baidu.com')
        WebDriverWait(self.driver, timeout=3)
        self.driver.switch_to.new_window('tab')

bot = imagebot()
bot.open()


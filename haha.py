from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import imageio

class imagebot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open(self):
        self.driver.get('https://www.metmuseum.org/art/collection/search#!?showOnly=openAccess&material=Oil%20paint%7CPaintings&geolocation=Europe&offset=0&pageSize=0&perPage=80&sortBy=Relevance&sortOrder=asc&searchField=All')
    def get_picture(self,i):
        WebDriverWait(self.driver,timeout=10).until(lambda d: d.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div[1]/div[{}]/a'.format(str(i+1))))
        picture = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div[1]/div[{}]/a'.format(str(i+1)))
        ref = picture.get_attribute('href')
        self.driver.switch_to.new_window('tab')
        self.driver.get(ref)
        WebDriverWait(self.driver,timeout=10).until(lambda d: d.find_element_by_xpath('//*[@id="the-artwork__inset"]/figure/div[2]/ul/li[2]/a'))
        new_picture = self.driver.find_element_by_xpath('//*[@id="the-artwork__inset"]/figure/div[2]/ul/li[2]/a')
        reff = new_picture.get_attribute('href')
        try:
            print('reading image #{}'.format(str(i)))
            buffer = imageio.imread(reff)
            print('writing image #{}'.format(str(i)))
            imageio.imwrite('test/test{}.jpg'.format(str(i)),buffer)
        except:
            print('one pic error!')
        self.driver.close()
    def next_page(self):
        WebDriverWait(self.driver,timeout=10).until(lambda d: d.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div[2]/ul/li[3]/button'))
        next_page_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div[2]/ul/li[3]/button')
        next_page_button.click()
        WebDriverWait(self.driver, timeout=3)

bot = imagebot()
bot.open()
original_window = bot.driver.current_window_handle
for count in range(2):
    for i in range(1,81):
        bot.get_picture(i)
        bot.driver.switch_to.window(original_window)
    bot.next_page()

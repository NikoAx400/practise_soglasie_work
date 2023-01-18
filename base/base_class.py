import datetime
from selenium import webdriver



class Base():


    def __init__(self, driver):
        self.driver = driver

    """получение текущего url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('текущая url ' + get_url)


    # def base_url_adress(self):
    #     base_url = 'https://www.soglasie.ru/'
    #     self.driver.get(base_url)
    #     self.driver.maximize_window()
    #
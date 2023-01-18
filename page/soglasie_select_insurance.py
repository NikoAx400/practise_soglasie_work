from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base

class soglasiePage(Base):

    base_url = 'https://www.soglasie.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # locators

    buy_polis = "//*[contains(@class, 'header__bottom-buttons')]//*[text() = 'Купить полис']"
    select_osago = "//*[contains(@class, 'col-sm-12')]//*[contains(@class, 'card services')]//*[text() = 'ОСАГО']"


    # GETTERS

    def get_buy_polis(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_polis)))

    def get_select_osago(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_osago)))

    # ACTIONS

        # клик по кнопке "Купить полис"
    def click_buy_polis(self):
        self.get_buy_polis().click()

        # клик по пункту "ОСАГО"
    def click_select_osago(self):
        self.get_select_osago().click()


    # METHODS

    def select_buy_polis(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.click_buy_polis()
        self.click_select_osago()

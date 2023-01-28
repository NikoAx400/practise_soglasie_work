from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
import allure
import time


class soglasie_policyholder_date(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # LOCATORS

    type_identification_number_field = "//*[contains(@class, 'step insurant')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Тип идентификационного номера']/following-sibling::*[contains(@class, 'select')]//input"
    type_vin = "//*[contains(@class, 's-select__list')]//*[contains(@class, 'vuebar-element')]//ul//li[text() = 'VIN']"
    type_number_chassis = "//*[contains(@class, 's-select__list')]//*[contains(@class, 'vuebar-element')]//ul//li[text() = 'Номер шасси']"
    type_body = "//*[contains(@class, 's-select__list')]//*[contains(@class, 'vuebar-element')]//ul//li[text() = 'Номер кузова']"

    identification_number_field = "//*[contains(@class, 'step insurant')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Идентификационный номер']/following-sibling::*[contains(@class, 'input')]//input"
    email_field = "//*[contains(@class, 'step insurant')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'E-mail']/following-sibling::*[contains(@class, 'input')]//input"
    telephone_field = "//*[contains(@class, 'step insurant')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Телефон']/following-sibling::*[contains(@class, 'input')]//input"

    continue_btn = "//*[text() = 'Далее']"

    # GETTERS

    def get_type_identification_number_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_identification_number_field)))

    def get_type_vin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_vin)))

    def get_type_number_chassis(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_number_chassis)))

    def get_type_body(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_body)))

    def get_identification_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.identification_number_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_telephone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone_field)))


    # ACTIONS

    def input_type_identification_number(self):
        self.get_type_identification_number_field().click()
        time.sleep(1)
        self.get_type_body().click()
        self.get_type_identification_number_field().click()

        # Заполнить поле "Идентификационный номер"
    def input_identification_number(self, intnum):
        self.get_identification_number().click()
        self.get_identification_number().send_keys(intnum)

        # Заполнить поле "e-mail"
    def input_email(self, mail):
        self.get_email_field().click()
        self.get_email_field().send_keys(mail)

        # Заполнить поле "Телефон"
    def input_telephone(self, numtel):
        self.get_telephone_field().click()
        self.get_telephone_field().send_keys(numtel)


    # METHODS

    def select_policyholder_date(self):
        with allure.step("select_policyholder_date"):

            self.input_type_identification_number()
            self.input_identification_number('12345678978945612358')
            self.input_email('moe_soglasie@mail.ru')
            self.input_identification_number('123456789')
            self.input_telephone('852345858')


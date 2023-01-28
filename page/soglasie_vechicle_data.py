from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.base_class import Base
import datetime
import allure
import time

class vechicle_data(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # LOCATORS

    calculation_not_number = "//*[contains(@class, 'content-center')]//*[contains(@class, 'avtokod')]//*[text() = 'Расчёт без ввода номера']"
    select_name_car = "//*[contains(@class, 'tabs__body')]//*[contains(@class, 'car-list')]//*[text() = 'Honda']"
    select_model_car = "//*[contains(@class, 'tabs__body')]//*[contains(@class, 'car-list')]//*[text() = 'CIVIC']"
    start_year = "//*[contains(@class, 'step specifications')]//*[contains(@class, 'step__content')]//*[contains(@class, 'box box-mb40')]//*[contains(@class, 'col')]//*[text() = 'Год выпуска']/following-sibling::*[contains(@class, 'select')]//input"
    power_field = "//*[contains(@class, 'step specifications')]//*[contains(@class, 'step__content')]//*[contains(@class, 'box box-mb40')]//*[contains(@class, 'col')]//*[text() = 'Мощность (л.с.)']/following-sibling::*[contains(@class, 'input-field')]//input"
    polis_start_date = "//*[contains(@class, 'step specifications')]//*[contains(@class, 'step__content')]//*[contains(@class, 'box box-mb40')]//*[contains(@class, 'col')]//*[text() = 'Дата начала действия полиса']/following-sibling::*[contains(@class, 'input')]//input"
    city_registration = "//*[contains(@class, 'step specifications')]//*[contains(@class, 'step__content')]//*[contains(@class, 'box box-mb40')]//*[contains(@class, 'col')]//*[text() = 'Город регистрации собственника']/following-sibling::*[contains(@class, 'input')]//input"
    continue_btn = "//*[text() = 'Далее']"

    # GETTERS

    def get_calculation_not_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calculation_not_number)))

    def get_select_name_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_name_car)))

    def get_select_model_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_model_car)))

    def get_select_start_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_year)))

    def get_power_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.power_field)))

    def get_polis_start_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.polis_start_date)))

    def get_city_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_registration)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # ACTIONS

        #Нажать на "Расчет без ввода номера"
    def click_calculation_not_number(self):
        self.get_calculation_not_number().click()

        # Выбор название марки автомобиля
    def click_select_name_car(self):
        self.get_select_name_car().click()

        # Нажать кнопку "далее"
    def press_continue_btn(self):
        self.get_continue_btn().click()

        # Выбор название модели автомобиля
    def click_select_model_car(self):
        self.get_select_model_car().click()

        # Заполнить поле "Мощность (л.с.)"
    def input_power_field(self, power_value):
        self.get_power_field().click()
        self.get_power_field().send_keys(power_value)

        # Заполнить поле "Год выпуска"
    def input_start_year(self):
        current_date = datetime.datetime.now()
        current_year = current_date.strftime('%Y')
        self.get_select_start_year().send_keys(current_year)

        # Заполнить поле "Дата начала действия полиса"
    def input_polis_start_date(self):
        current_date = datetime.datetime.now() + datetime.timedelta(days=1)
        date_polis = current_date.strftime('%d.%m.%Y')
        self.get_polis_start_date().send_keys(date_polis)

        # Заполнить поле "Город регистрации собственника"
    def input_city_registration(self, place_registration):
        self.get_city_registration().click()
        self.get_city_registration().send_keys(place_registration)
        time.sleep(1)
        self.get_city_registration().send_keys(Keys.ENTER)


    # METHODS

    def select_car(self):
        with allure.step("select_car"):

            self.click_calculation_not_number()
            self.click_select_name_car()
            self.click_select_model_car()
            self.input_start_year()
            self.input_power_field('130')
            self.input_polis_start_date()
            self.input_city_registration('Москва')
            self.press_continue_btn()

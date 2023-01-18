from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page.soglasie_vechicle_data import vechicle_data
from base.base_class import Base
import datetime
import time

class use_car_period(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver


    # LOCATORS

    year_switch = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Год']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher')]"
    select_period_switch = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Выбрать период']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher')]"

    type_insurance_field = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Тип страхования']/following-sibling::*[contains(@class, 'select')]//input"
    type_insurance_20_days = f"//*[contains(@class, 's-select__list-select-holder')]//ul//li[text() = '20']"
    type_insurance_1_year = "//*[contains(@class, 's-select__list-select-holder')]//ul//li[text() = 'Обычный договор сроком действия 1 год']"

    purpose_use_car_field = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Цель использования ТС']/following-sibling::*[contains(@class, 'input')]//input"
    policy_start_date_field = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата начала действия полиса']/following-sibling::*[contains(@class, 'input')]//input"
    policy_finish_date_field = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата окончания действия полиса']/following-sibling::*[contains(@class, 'input')]//input"

    continue_btn = "//*[text() = 'Далее']"

    # GETTERS

    def get_type_insurance_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_insurance_field)))

    def get_type_insurance_20_days(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_insurance_20_days)))

    def get_type_insurance_1_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_insurance_1_year)))

    def get_purpose_use_car_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.purpose_use_car_field)))

    def get_policy_start_date_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.policy_start_date_field)))

    def get_policy_finish_date_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.policy_finish_date_field)))

    def get_year_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_switch)))

    def get_select_period_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_period_switch)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # ACTIONS

        # Активировать переключатель на "Выбрать период"
    def click_select_period_switch(self):
        self.get_select_period_switch().click()

        # Активировать переключатель на "Год"
    def click_year_switch(self):
        self.get_year_switch().click()

        # Нажать на кнопку на "Далее"
    def press_continue_btn(self):
        self.get_continue_btn().click()

        # Из выпадающего списка выбрать "Следовать к месту регистрации..."
    def select_type_insurance_20days(self):
        self.get_type_insurance_field().click()
        time.sleep(1)
        type_insuranse_20 = self.get_type_insurance_20_days().click()
        return type_insuranse_20

        # Из выпадающего списка выбрать "Обычный договор..."
    def select_type_insurance_1year(self):
        self.get_type_insurance_field().click()
        time.sleep(1)
        type_insuranse_1 =  self.get_type_insurance_1_year().click()
        return type_insuranse_1

        # Проверка значения в поле "Тип страхования"
    def value_type_insurance(self, correct_insurance):
        value_insurance = self.get_type_insurance_field().get_attribute('value')
        correct_value = correct_insurance
        assert value_insurance == correct_value
        print(value_insurance)

        # Проверка значения в поле "Цель использования ТС"
    def value_purpose_use_car(self, correct_use):
        value_purpose_use_car = self.get_purpose_use_car_field().get_attribute('value')
        correct_value_use = correct_use
        assert value_purpose_use_car == correct_value_use
        print(value_purpose_use_car)

        # Проверка значений в полях "Дата начала действия полиса" и "Дата окончания действия полиса"
        # При использовании страхования на год, разница 1.
    def value_start_finish_action_polis(self):
        value_start_action_polis = self.get_policy_start_date_field().get_attribute('value')
        value_policy_finish_date_field = self.get_policy_finish_date_field().get_attribute('value')
        start_action_polis = list(value_start_action_polis.split('.'))
        policy_finish = list(value_policy_finish_date_field.split('.'))
        assert (int(policy_finish[-1]) - int(start_action_polis[-1])) == 1


    # METHODS

    def select_period_use_car(self):

        self.select_type_insurance_1year()
        self.value_type_insurance('Обычный договор сроком действия 1 год')
        self.value_purpose_use_car('Личные')
        self.value_start_finish_action_polis()
        self.press_continue_btn()


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
import time

class soglasie_data_check(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # locators
    tab_specifications = "//*[contains(@class, 'step specifications')]//*[text() = 'Характеристики']/following-sibling::*[contains(@class, 'edit-btn')]//*[text() = 'Изменить']"
    polis_start_date = "//*[contains(@class, 'step specifications')]//*[contains(@class, 'step__content')]//*[contains(@class, 'box box-mb40')]//*[contains(@class, 'col')]//*[text() = 'Дата начала действия полиса']/following-sibling::*[contains(@class, 'input')]//input"

    tab_drivers = "//*[contains(@class, 'step drivers')]//*[text() = 'Водители']/following-sibling::*[contains(@class, 'edit-btn')]//*[text() = 'Изменить']"
    full_name_field = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Фамилия Имя Отчество']/following-sibling::*[contains(@class, 'input')]//input"
    date_birth_field = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата рождения']/following-sibling::*[contains(@class, 'input')]//input"

    tab_exploitation = "//*[contains(@class, 'step exploitation')]//*[text() = 'Использование']/following-sibling::*[contains(@class, 'edit-btn')]//*[text() = 'Изменить']"
    policy_start_date_field = "//*[contains(@class, 'step__content')]//*[contains(@class, 'exploitation')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата начала действия полиса']/following-sibling::*[contains(@class, 'input')]//input"

    tab_owner = "//*[contains(@class, 'step owner')]//*[text() = 'Собственник']/following-sibling::*[contains(@class, 'edit-btn')]//*[text() = 'Изменить']"
    full_name_owner_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Фамилия Имя Отчество']/following-sibling::*[contains(@class, 'input')]//input"
    date_birth_owner_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата рождения']/following-sibling::*[contains(@class, 'input')]//input"

    start_year = "//*[contains(@class, 'step specifications')]//*[contains(@class, 'step__content')]//*[contains(@class, 'box box-mb40')]//*[contains(@class, 'col')]//*[text() = 'Год выпуска']/following-sibling::*[contains(@class, 'select')]//input"
    date_issue = "//*[contains(@class, 'step registration')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата начала действия полиса']/following-sibling::*[contains(@class, 'input')]//input"


    # getters

    def get_specifications(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_specifications)))
    def get_polis_start_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.polis_start_date)))


    def get_drivers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_drivers)))
    def get_full_name_drivers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name_field)))
    def get_date_birth_drivers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_birth_field)))


    def get_exploitation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_exploitation)))
    def get_policy_start_date_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.policy_start_date_field)))


    def get_owner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_owner)))
    def get_full_name_owner_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name_owner_field)))
    def get_date_birth_owner_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_birth_owner_field)))

    # Actions

    # Раскрыть раздел "Характеристики"
    def click_specifications(self):
        self.get_specifications().click()

    # Раскрыть раздел "Водители"
    def click_drivers(self):
        self.get_drivers().click()

    # Раскрыть раздел "Использование"
    def click_exploitation(self):
        self.get_exploitation().click()

    # Раскрыть раздел "Собственник"
    def click_owner(self):
        self.get_owner().click()

    # Получение значения из поля  - дата начала действия полиса (Характеристики)
    def value_start_specifications_polis(self):
        value_start_cpec_polis = self.get_polis_start_date().get_attribute('value')
        return value_start_cpec_polis

    # Получение значения из поля  - дата начала действия полиса (Использование)
    def value_start_exploitation_polis(self):
        value_start_exp_polis = self.get_policy_start_date_field().get_attribute('value')
        return value_start_exp_polis

    # Получение значения из поля  - ФИО (Водители)
    def value_full_name_drivers(self):
        value_full_name = self.get_full_name_drivers().get_attribute('value')
        return value_full_name

    # Получение значения из поля  - дата рождения (Водители)
    def value_date_birth_drivers(self):
        value_date_birth = self.get_date_birth_drivers().get_attribute('value')
        return value_date_birth

    # Получение значения из поля  - ФИО (Собственник)
    def value_full_name_owner(self):
        value_name_owner = self.get_full_name_owner_field().get_attribute('value')
        return value_name_owner

    # Получение значения из поля  - дата рождения (Собственник)
    def value_birth_owner(self):
        value_birth_owner = self.get_date_birth_owner_field().get_attribute('value')
        return value_birth_owner

    # Methods

    def data_check(self):

        self.click_specifications()
        date_cpec_polis = self.value_start_specifications_polis()
        time.sleep(2)

        self.click_drivers()
        name_drivers = self.value_full_name_drivers()
        birth_drivers = self.value_date_birth_drivers()
        time.sleep(2)

        self.click_exploitation()
        start_exp_polis = self.value_start_exploitation_polis()
        time.sleep(2)

        self.click_owner()
        name_owner = self.value_full_name_owner()
        birh_owner = self.value_birth_owner()
        time.sleep(2)

        """Производится сверка ФИО и даты рождения в разделе Водители и Собственника на предмет идентичности, т.к. тест
                предполагает, что страхователь/водитель/собственник одно и то же лицо"""
        assert name_drivers == name_owner
        assert birth_drivers == birh_owner
        """Производится сверка даты начала действия полиса из раздела 
        Характеристики и Использования на предмет идентичности"""
        assert date_cpec_polis == start_exp_polis





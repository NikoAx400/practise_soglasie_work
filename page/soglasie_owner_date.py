from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.base_class import Base
import allure
import time

class owner_data(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # LOCATORS

    owner_policyholder = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Собственник является страхователем']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher _one-side')]"
    man_checkbox = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Пол']/following-sibling::*[contains(@class, 'radio')]//*[text() = 'Мужчина']"
    woman_checkbox = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Пол']/following-sibling::*[contains(@class, 'radio')]//*[text() = 'Женщина']"

    full_name_owner_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Фамилия Имя Отчество']/following-sibling::*[contains(@class, 'input')]//input"
    date_birth_owner_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата рождения']/following-sibling::*[contains(@class, 'input')]//input"
    date_issue_passport_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата выдачи']/following-sibling::*[contains(@class, 'input')]//input"
    series_number_passport_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Серия и номер Паспорта РФ']/following-sibling::*[contains(@class, 'input')]//input"
    issued_by_passport_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Кем выдан']/following-sibling::*[contains(@class, 'input')]//input"
    adress_field = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Адрес']/following-sibling::*[contains(@class, 'input')]//input"
    active_drop_down_list = "//*[contains(@class, 'step owner')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Адрес']/following-sibling::*//*[contains(@class, 'active')]"

    continue_btn = "//*[text() = 'Далее']"

    # GETTERS

    def get_owner_policyholder_swich(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.owner_policyholder)))

    def get_full_name_owner_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name_owner_field)))

    def get_date_birth_owner_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_birth_owner_field)))

    def get_date_issue_passport_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_issue_passport_field)))

    def get_series_number_passport_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.series_number_passport_field)))

    def get_issued_by_passport_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.issued_by_passport_field)))

    def get_adress_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_field)))

    def get_active_drop_down_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.active_drop_down_list)))

    def get_owner_policyholder_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.owner_policyholder)))

    def get_man_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.man_checkbox)))

    def get_woman_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.woman_checkbox)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # ACTIONS

        # Актировать переключатьель "Собстаенник является страхователем"
    def owner_policyholder_swich(self):
        self.get_owner_policyholder_swich().click()

        # Актировать радиокнопку "Мужчина"
    def click_select_man(self):
        self.get_man_checkbox().click()

        # Актировать радиокнопку "Женщина"
    def click_select_woman(self):
        self.get_woman_checkbox().click()

        # Нажать кнопку "Далее"
    def press_continue_btn(self):
        self.get_continue_btn().click()

        # Заполнить поле "Серия и номер паспорта РФ"
    def input_series_number_passport(self, passport):
        self.get_series_number_passport_field().click()
        self.get_series_number_passport_field().send_keys(passport)

        # Заполнить поле "Дата выдачи"
    def input_date_issue_passport(self, issue_passport):
        self.get_date_issue_passport_field().click()
        self.get_date_issue_passport_field().send_keys(issue_passport)

        # Заполнить поле "Кем выдан"
    def input_issued_by_passport(self, passport_date):
        self.get_issued_by_passport_field().click()
        self.get_issued_by_passport_field().send_keys(passport_date)

        # Заполнить поле "Адрес"
    def input_adress_field(self, adress):
        self.get_adress_field().click()
        self.get_adress_field().send_keys(adress)
        self.get_active_drop_down_list()
        time.sleep(1)
        self.get_adress_field().send_keys(Keys.ENTER)
        time.sleep(1)


    # METHODS

    def owner_date(self):
        with allure.step("owner_date"):

            self.owner_policyholder_swich()
            self.click_select_woman()
            self.input_series_number_passport('45 05 454545')
            self.input_date_issue_passport('10.01.2019')
            self.input_issued_by_passport('город Москва')
            self.input_adress_field(', ул Лесная, д 5, кв 45')
            self.press_continue_btn()


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base

class drivers_data(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # LOCATORS

    unlimited_amount_drivers_switch = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Неограниченное количество водителей']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher _one-side')]"
    driver_insured_switch = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Водитель является страхователем']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher _one-side')]"
    start_year_experience_switch = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Год начала стажа']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher')]"
    experience_switch = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Стаж (полных лет)']/ancestor-or-self::*[contains(@class, 'switcher')]//*[contains(@class, 'switcher__switcher')]"
    man_checkbox = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Пол']/following-sibling::*[contains(@class, 'radio')]//*[text() = 'Мужчина']"
    woman_checkbox = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Пол']/following-sibling::*[contains(@class, 'radio')]//*[text() = 'Женщина']"

    full_name_field = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Фамилия Имя Отчество']/following-sibling::*[contains(@class, 'input')]//input"
    date_birth_field = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата рождения']/following-sibling::*[contains(@class, 'input')]//input"
    date_issue_driver_lisense = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата выдачи']/following-sibling::*[contains(@class, 'input')]//input"
    series_number_driver_lisense = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Серия и номер ВУ']/following-sibling::*[contains(@class, 'input')]//input"
    start_year_experience_field = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Год начала стажа']/following-sibling::*[contains(@class, 'input')]//input"
    experience_field = "//*[contains(@class, 'drivers')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Стаж (полных лет)']/following-sibling::*[contains(@class, 'input')]//input"

    continue_btn = "//*[text() = 'Далее']"

    # GETTERS

    def get_full_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name_field)))

    def get_date_birth_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_birth_field)))

    def get_date_issue_driver_lisense(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_issue_driver_lisense)))

    def get_series_number_driver_lisense(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.series_number_driver_lisense)))

    def get_start_year_experience_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_year_experience_field)))

    def get_experience_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.experience_field)))


    def get_unlimited_amount_drivers_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.unlimited_amount_drivers_switch)))

    def get_driver_insured_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.driver_insured_switch)))

    def get_start_year_experience_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_year_experience_switch)))

    def get_experience_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.experience_switch)))

    def get_man_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.man_checkbox)))

    def get_woman_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.woman_checkbox)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # ACTIONS

        # Изменить переключатель "Водитель является страхователем"
    def click_driver_insured_switch(self):
        self.get_driver_insured_switch().click()

        # Активировать радиокнопку "Мужчина"
    def click_select_man(self):
        self.get_man_checkbox().click()

        # Активировать радиокнопку "Женщина"
    def click_select_woman(self):
        self.get_woman_checkbox().click()

        # Изменить переключатель "Стаж (полных лет)"
    def click_experience_switch(self):
        self.get_experience_switch().click()

        # Изменить переключатель "Год начала стажа"
    def click_start_year_experience_switch(self):
        self.get_start_year_experience_switch().click()

        # Нажать кнопку "Далее"
    def press_continue_btn(self):
        self.get_continue_btn().click()

        # Заполнить поле "Фамилия Имя Отчество"
    def input_full_name_field(self, full_name):
        self.get_full_name_field().click()
        self.get_full_name_field().send_keys(full_name)

        # Заполнить поле "Дата рождения"
    def input_date_birth_field(self, birth_date):
        self.get_date_birth_field().click()
        self.get_date_birth_field().send_keys(birth_date)

        # Заполнить поле "Серия и номер ВУ"
    def input_series_number_driver_lisense(self, driver_lisense):
        self.get_series_number_driver_lisense().click()
        self.get_series_number_driver_lisense().send_keys(driver_lisense)

        # Заполнить поле "дата выдачи"
    def input_date_issue_driver_lisense(self, lisense_date):
        self.get_date_issue_driver_lisense().click()
        self.get_date_issue_driver_lisense().send_keys(lisense_date)

        # Заполнить поле "Стаж (полных лет)"
    def input_experience_field(self, experience):
        self.get_experience_switch().click()
        self.get_experience_field().send_keys(experience)

        # Заполнить поле "Год начала стажа"
    def input_start_year_experience_field(self, start_experience):
        self.get_start_year_experience_switch().click()
        self.get_start_year_experience_field().send_keys(start_experience)


    # METHODS

    def select_drivers_date(self):

        self.click_driver_insured_switch()
        self.click_select_woman()
        self.input_full_name_field('Карпова Карина Кариновна')
        self.input_date_birth_field('10.02.1988')
        self.input_series_number_driver_lisense('1988 856255')
        self.input_date_issue_driver_lisense('10.02.2010')
        self.input_experience_field('5')
        self.press_continue_btn()


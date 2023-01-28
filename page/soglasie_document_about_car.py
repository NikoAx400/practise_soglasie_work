from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
import allure
import datetime

class data_document_car(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self. driver = driver

    # LOCATORS

    registration_plate_field = "//*[contains(@class, 'step registration')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Гос. регистрационный знак']/following-sibling::*[contains(@class, 'input')]//input"
    serial_number_ctc = "//*[contains(@class, 'step registration')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Серия и номер СТС']/following-sibling::*[contains(@class, 'input')]//input"
    date_issue = "//*[contains(@class, 'step registration')]//*[contains(@class, 'box')]//*[contains(@class, 'col')]//*[text() = 'Дата выдачи']/following-sibling::*[contains(@class, 'input')]//input"

    continue_btn = "//*[text() = 'Далее']"

    # GETTERS

    def get_registration_plate_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_plate_field)))

    def get_serial_number_ctc_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.serial_number_ctc)))

    def get_date_issue_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_issue)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))


    # ACTIONS

        # Нажать на кнопку "Далее"
    def press_continue_btn(self):
        self.get_continue_btn().click()

        # Заполнить поле "Гос.регистрационный знак"
    def input_registration_plate(self, registration_plate):
        self.get_registration_plate_field().click()
        self.get_registration_plate_field().send_keys(registration_plate)

        # Заполнить поле "Серия и номер СТС"
    def input_serial_number_ctc(self, serial_number_ctc):
        self.get_serial_number_ctc_field().click()
        self.get_serial_number_ctc_field().send_keys(serial_number_ctc)

        # Заполнить поле "Дата выдачи"
    def input_date_issue(self):
        current_date = datetime.datetime.now() + datetime.timedelta(days=-1)
        date_issue_plate = current_date.strftime('%d.%m.%Y')
        self.get_date_issue_field().click()
        self.get_date_issue_field().send_keys(date_issue_plate)


    # METHODS

    def document_car(self):
        with allure.step("document_car"):

            self.input_registration_plate('А 123 АВ 199')
            self.input_serial_number_ctc('1234 567895')
            self.input_date_issue()
            self.press_continue_btn()

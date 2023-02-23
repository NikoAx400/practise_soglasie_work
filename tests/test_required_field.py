from page.soglasie_select_insurance import soglasiePage
from page.soglasie_vechicle_data import vechicle_data
from selenium import webdriver
import allure

@allure.description("test_amerging_notice")
def test_amerging_notice(set_up):

    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\resourse\\chromedriver.exe')

    # 1. Выбор полиса ОСАГО на главной странице СК Согласие
    soglasie = soglasiePage(driver)
    soglasie.select_buy_polis()
    soglasie.click_select_osago()

    # 2. Выбор марки модели и заполнение раздела "Характристики"
    selection_car = vechicle_data(driver)
    selection_car.presence_notification_select_car()


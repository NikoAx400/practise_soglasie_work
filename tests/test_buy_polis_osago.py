from page.soglasie_data_check import soglasie_data_check
from page.soglasie_document_about_car import data_document_car
from page.soglasie_drivers_date import drivers_data
from page.soglasie_owner_date import owner_data
from page.soglasie_period_use_car import use_car_period
from page.soglasie_policyholder_date import soglasie_policyholder_date
from page.soglasie_select_insurance import soglasiePage
from page.soglasie_vechicle_data import vechicle_data
from selenium import webdriver




def test_buy_polis_osago(set_up):

    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\resourse\\chromedriver.exe')

    # 1. Выбор полиса ОСАГО на главной странице СК Согласие
    soglasie = soglasiePage(driver)
    soglasie.select_buy_polis()
    soglasie.click_select_osago()

    # 2. Выбор марки модели и заполнение раздела "Характристики"
    selection_car = vechicle_data(driver)
    selection_car.select_car()

    # 3. Заполнение раздела "Водители"
    drivers_car = drivers_data(driver)
    drivers_car.select_drivers_date()

    # 4. Заполнение и проверка раздела "Использование"
    use_car = use_car_period(driver)
    use_car.select_period_use_car()

    # 5. Заполнение раздела "Документы о регистрации ТС"
    document_car = data_document_car(driver)
    document_car.document_car()

    # 6. Заполнение и проверка раздела "Собственник"
    owner = owner_data(driver)
    owner.owner_date()

    # 7. Заполнение раздела "Страхователь"
    policyholder = soglasie_policyholder_date(driver)
    policyholder.select_policyholder_date()

    # 8. Проверка идентичности ФИО, даты рождения и начала действия полисов
    check_soglasie = soglasie_data_check(driver)
    check_soglasie.data_check()

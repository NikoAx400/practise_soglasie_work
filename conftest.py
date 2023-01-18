import pytest
from selenium import webdriver



# @pytest.fixture()
# def set_up():
#     driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\resourse\\chromedriver.exe')
#     print('start test')
#     driver.maximize_window()
#     base_url = 'https://www.soglasie.ru/'
#     driver.get(base_url)
#
#     yield driver
#
#     print('finish test')

@pytest.fixture()
def set_up():
    print('start test')


    yield

    print('finish test')
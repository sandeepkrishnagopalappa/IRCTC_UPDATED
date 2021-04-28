import pytest
from Library.web_utility import GenericMethod
from Library.file_library import ReadJson
from config import *
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path, options=options)


@pytest.fixture(scope='class', autouse=True)
def driver_init():
    driver.implicitly_wait(30)
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()



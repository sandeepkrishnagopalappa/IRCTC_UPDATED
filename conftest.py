import pytest
from Library.web_utility import GenericMethod
from Library.file_library import ReadJson
from config import *
from selenium import webdriver

""" This is the conftest file which contains commonly used file in all pages """

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path, options=options)


@pytest.fixture(scope='class', autouse=True)
def driver_init():
    """ This is the method where i have used fixtures in it. """
    driver.implicitly_wait(30)
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()


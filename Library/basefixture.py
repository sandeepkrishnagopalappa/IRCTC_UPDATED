""" This is basefixture  """

import pytest
from selenium import webdriver
from config import *

class Driver_init:
    """ This is the class where we create fixture and this fixture is like a decorator """

    @pytest.fixture(scope='class',autouse=True)
    def driver_init(self,request):
        """ Request holds the information of the method that is currently calling the fixture
            This function is used to lanch the browser  """

        if browser.upper()=="CHROME":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            driver=webdriver.Chrome(executable_path,options=options)

        elif browser.upper()=="FIREFOX":
            driver=webdriver.Firefox()

        request.cls.driver=driver
        driver.implicitly_wait(20)
        driver.get(url)
        driver.maximize_window()
        yield
        driver.quit()

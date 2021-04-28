from conftest import *

class Register():

    def __init__(self, driver):
        self.driver = driver
        self.variable1 =ReadJson.read_locators(OBJECT_JSON)
        self.ObjectGen = GenericMethod()

    def alert_ok(self):
        self.ObjectGen.click_on_element(self.driver, self.variable1["alert_ok"])

    def click_on_flight(self):
        self.ObjectGen.click_on_element(self.driver, self.variable1["click_on_flight"])

    def window_switch(self):
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        return self.ObjectGen.get_page_title(self.driver)
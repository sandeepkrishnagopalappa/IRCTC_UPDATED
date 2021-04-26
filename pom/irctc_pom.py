from Library.web_utility import GenericMethod
from Library.file_library import XlData
from Library.basefixture import *


class Register(Driver_init):
    data = XlData()
    variable1, keys = data.read_locators(file_name, sheet_name)
    ObjectGen = GenericMethod()

    def __init__(self, driver):
        self.driver = driver

    def alert_ok(self):
        reg1 = Register.variable1["alert_ok"]
        Register.ObjectGen.click_on_element(self.driver, reg1)

    def click_on_flight(self):
        reg2 = Register.variable1["click_on_flight"]
        Register.ObjectGen.click_on_element(self.driver, reg2)

    def window_switch(self):
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        return self.ObjectGen.get_page_title(self.driver)


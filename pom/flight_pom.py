
from Library.web_utility import GenericMethod
from Library.file_library import XlData
from Library.basefixture import *

class FlightRegister(Driver_init):

    data_ = XlData()
    variable1_, keys_ = data_.read_locators(file_name, sheet_name)
    ObjectGen_ = GenericMethod()

    def __init__(self, driver):
        self.driver = driver

    def pop_up_ok(self):
        reg_pop = FlightRegister.variable1_["pop_up_ok"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg_pop)

    def round_trip(self):
        reg3 = FlightRegister.variable1_["round_trip"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg3)
        return FlightRegister.ObjectGen_.validate_element_display(self.driver, FlightRegister.variable1_["return_date_click"])

    def station_from_sending_keys(self):
        reg4 = FlightRegister.variable1_["station_from_sending_keys"]
        FlightRegister.ObjectGen_.enter_text(self.driver, reg4, values="Chennai")

    def station_from_click(self):
        reg5 = FlightRegister.variable1_["station_from_click"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg5)

    def station_to_sending_keys(self):
        reg6 = FlightRegister.variable1_["station_to_sending_keys"]
        FlightRegister.ObjectGen_.enter_text(self.driver, reg6, values="Mumbai")

    def station_to_click(self):
        reg7 = FlightRegister.variable1_["station_to_click"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg7)

    def start_date_select(self):
        reg8 = FlightRegister.variable1_["start_date_select"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg8)

    def return_date_click(self):
        reg9 = FlightRegister.variable1_["return_date_click"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg9)

    def apirl_month_select(self):
        reg10 = FlightRegister.variable1_["apirl_month_select"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg10)

    def return_date_select(self):
        reg11 = FlightRegister.variable1_["return_date_select"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg11)

    def search(self):
        reg12 = FlightRegister.variable1_["search"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg12)
        return FlightRegister.ObjectGen_.validate_element_display(self.driver, FlightRegister.variable1_["book"])

    def book(self):
        reg13 = FlightRegister.variable1_["book"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg13)
        return FlightRegister.ObjectGen_.validate_element_display(self.driver, FlightRegister.variable1_["gst_pop_up"])

    def normal_fair(self):
        reg14 = FlightRegister.variable1_["continue"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg14)

    def gst_pop_up(self):
        reg15 = FlightRegister.variable1_["gst_pop_up"]
        FlightRegister.ObjectGen_.click_on_element(self.driver, reg15)

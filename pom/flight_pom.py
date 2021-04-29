from pom import *


class FlightRegister():

    def __init__(self, driver, first, second):
        self.driver = driver
        self.first = first
        self.second= second
        self.variable1_ = ReadJson.read_locators(OBJECT_JSON)
        self.ObjectGen_ = GenericMethod()

    def pop_up_ok(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["pop_up_ok"])

    def round_trip(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["round_trip"])
        return self.ObjectGen_.validate_element_display(self.driver,self.variable1_["return_date_click"])

    def station_from_sending_keys(self):
        self.ObjectGen_.enter_text(self.driver, self.variable1_["station_from_sending_keys"],self.first)
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["station_from_click"])

    def station_to_sending_keys(self):
        self.ObjectGen_.enter_text(self.driver, self.variable1_["station_to_sending_keys"],self.second)
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["station_to_click"])

    def start_date_select(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["start_date_select"])

    def return_date_click_select(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["return_date_click"])
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["apirl_month_select"])
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["return_date_select"])

    def search(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["search"])
        return self.ObjectGen_.validate_element_display(self.driver,self.variable1_["book"])

    def book_button_click(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["book"])

    def normal_fair(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["continue"])
        return self.ObjectGen_.validate_element_display(self.driver, self.variable1_["gst_pop_up"])

    def gst_pop_up(self):
        self.ObjectGen_.click_on_element(self.driver, self.variable1_["gst_pop_up"])

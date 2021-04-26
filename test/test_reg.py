"""  This page is the page where pytest detects automatically and
    through which all the methods or APIs are called through  """

from config import *
from pom.irctc_pom import Register
from pom.flight_pom import FlightRegister
from Library.basefixture import Driver_init

class Test_demo(Driver_init):

    def test_object(self):
        assert url == self.driver.current_url, "URL did not match"
        obj = Register(self.driver)
        obj.alert_ok()
        obj.click_on_flight()
        obj.window_switch()

    def test_object_flight(self):
        obj=FlightRegister(self.driver)
        obj.pop_up_ok()
        res_of_round_button= obj.round_trip()
        assert res_of_round_button == True, "Round trip radio button is not selected"
        obj.station_from_sending_keys()
        obj.station_from_click()
        obj.station_to_sending_keys()
        obj.station_to_click()
        obj.start_date_select()
        obj.return_date_click()
        obj.apirl_month_select()
        obj.return_date_select()
        self.res_of_search_button = obj.search()
        assert self.res_of_search_button == True, "Book button is not displayed"
        self.res_of_book_button=obj.book()
        assert self.res_of_search_button == True, "GST pop button not displayed"
        obj.gst_pop_up()








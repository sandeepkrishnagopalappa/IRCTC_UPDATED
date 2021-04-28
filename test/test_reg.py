import pytest
from pom.irctc_pom import Register
from pom.flight_pom import FlightRegister
from conftest import url,driver

@pytest.mark.usefixtures("driver_init")
class Test_demo:

    def test_object(self):

        assert url == driver.current_url, "URL did not match"
        obj_reg = Register(driver)
        obj_reg.alert_ok()
        obj_reg.click_on_flight()
        obj_reg.window_switch()

        obj=FlightRegister(driver)
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
        obj.normal_fair()
        assert self.res_of_search_button == True, "GST pop button not displayed"
        obj.gst_pop_up()










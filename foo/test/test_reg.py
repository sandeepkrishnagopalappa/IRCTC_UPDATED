from foo import *

@pytest.mark.usefixtures("driver_init")
class Test_demo():

    test_data = ReadJson.read_test_data(OBJECT_JSON_SEND)

    @pytest.mark.parametrize('first, second', test_data)
    def test_object(self, first, second):

        assert url == self.driver.current_url, "URL did not match"
        obj_reg = Register(self.driver)
        obj_reg.alert_ok()
        obj_reg.click_on_flight()
        obj_reg.window_switch()
        obj=FlightRegister(self.driver, first, second)
        obj.pop_up_ok()
        res_of_round_button= obj.round_trip()
        assert res_of_round_button == True, "Round trip radio button is not selected"
        obj.station_from_sending_keys()
        obj.station_to_sending_keys()
        obj.start_date_select()
        obj.return_date_click_select()
        self.res_of_search_button = obj.search()
        assert self.res_of_search_button == True, "Book button is not displayed"
        self.res_of_book_button=obj.book_button_click()
        obj.normal_fair()
        assert self.res_of_search_button == True, "GST pop button not displayed"
        obj.gst_pop_up()

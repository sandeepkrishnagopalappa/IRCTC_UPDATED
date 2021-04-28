"""module for all generic methods"""

class GenericMethod:
    """click, text, radio button, check box"""

    @staticmethod
    def click_on_element(driver,locator):
        """clicking element"""
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).click()

    @staticmethod
    def enter_text(driver,locator,*,values):
        """entering the text"""
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).send_keys(str(values))

    @staticmethod
    def validate_check_radio_button(driver,locator):
        """checking the checkbox"""
        locator_type, locator_value = locator
        return driver.find_element(locator_type, locator_value).is_selected()

    @staticmethod
    def validate_element_display(driver,locator):
        """validating"""
        locator_type, locator_value = locator
        return driver.find_element(locator_type, locator_value).is_displayed()

    @staticmethod
    def get_page_title(driver):
        """title"""
        return driver.title

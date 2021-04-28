import json
from config import *


data = {
    "alert_ok" : {"locatorType":"xpath",
                  "locatorValue":"//button[@class='btn btn-primary']"},

    "click_on_flight" : {"locatorType" : "xpath",
                         "locatorValue" : "//a[@aria-label='Menu Flight. Website will be opened in new tab']"},

    "pop_up_ok" : {"locatorType" : "xpath",
                         "locatorValue" : "//button[text()='Ok']"},

    "round_trip": {"locatorType": "xpath",
                 "locatorValue": "//label[@for='Round-Trip']"},

    "station_from_sending_keys": {"locatorType": "xpath",
                                    "locatorValue": "//input[@id='stationFrom']"},

    "station_from_click": {"locatorType": "xpath",
                                             "locatorValue": "//div[text()='Chennai (MAA)']"},

    "station_to_sending_keys": {"locatorType": "xpath",
                                      "locatorValue": "//input[@id='stationTo']"},

    "station_to_click": {"locatorType": "xpath",
                                           "locatorValue":"//div[text()='Mumbai (BOM)']"},

    "start_date_select": {"locatorType": "xpath",
                                           "locatorValue":"//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom rdeparturedate']//table[@class='date-table']//td//span[normalize-space(text())='30']"},

    "return_date_click": {"locatorType": "xpath",
                                     "locatorValue":"//input[@id='returnDate']"},

    "apirl_month_select": {"locatorType": "xpath",
                                     "locatorValue":"//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom returnDate']//div[@class='date-table-right']//span[normalize-space(text())='May' and @class='M-Month d-block d-md-none']/.."},

    "return_date_select": {"locatorType": "xpath",
                                      "locatorValue":"//span[normalize-space(text())='30' and @class='act']"},

    "search": {"locatorType": "xpath",
                                      "locatorValue":"//button[text()='Search ']"},

    "book": {"locatorType": "xpath",
                                      "locatorValue":"//button[text()='Book']"},

    "continue": {"locatorType": "xpath",
                        "locatorValue":"//button[text()='Continue  With  Normal Fare  ']"},

    "gst_pop_up": {"locatorType": "xpath",
                        "locatorValue":"//button[text()='No ']"}
}

with open(OBJECT_JSON, 'w+') as fileobj:
    json.dump(data, fileobj, indent=4)


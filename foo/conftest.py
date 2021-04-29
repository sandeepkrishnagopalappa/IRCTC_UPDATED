from foo import *

""" This is the conftest file which contains commonly used file in all pages """

@pytest.fixture(scope='class',autouse=True)
def driver_init(request):
    """ This is the method where i have used fixtures in it. """
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(executable_path, options=options)
    request.cls.driver= driver
    driver.implicitly_wait(30)
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()
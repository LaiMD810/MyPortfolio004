import pytest
from selenium import webdriver


@pytest.fixture(params=["Firefox","Chrome"])
def driverBrowser(request):
    browser = request.param
    if browser == "Chrome":

        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")  # create option that run in private mode
        driver = webdriver.Chrome(options=options)  # make the chromedriver to use created options
        driver.implicitly_wait(10)
    elif browser == "Firefox":

        options = webdriver.FirefoxOptions()
        options.add_argument("--incognito")  # create option that run in private mode
        driver = webdriver.Firefox(options=options)  # make the chromedriver to use created options
        driver.implicitly_wait(10)

    yield driver
    driver.quit()

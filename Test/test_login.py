import json

import pytest

from POM_Pages.LoginPage import LoginPage

testdatapath ='../TestData /LoginTestData.json'
with open(testdatapath) as f:
    test_data = json.load(f)["loginData"]

@pytest.mark.parametrize("loginData",test_data)
def test_login(driverBrowser,loginData): #using the json test data, and run the test in firefox and chrome browser
    driver = driverBrowser
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    loginPage = LoginPage(driver)
    loginPage.Login(loginData["username"],loginData["userpassword"])

    if  loginData["expected"] == "Success":
        loginPage.LoginSuccess()
    elif loginData["expected"] == "Failed":
        loginPage.LoginFailed(loginData["errorMessage"])
    elif loginData["expected"] == "Locked":
        loginPage.LoginLocked(loginData["errorMessage"])


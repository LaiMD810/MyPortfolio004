import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Login Page
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.loginButton = (By.ID,"login-button")
        self.errorMessage = (By.XPATH,"//div[@class='error-message-container error']")
        self.HomePage = (By.XPATH,"//span[@class='title']")

    def Login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginButton).click()


    def LoginSuccess(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.HomePage)
        )
        homePage = element.text
        assert "Products" in homePage

    def LoginFailed(self,expectedErrorMessage):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.errorMessage)
        )
        errorMessage = element.text
        print(errorMessage)
        print("done")
        assert expectedErrorMessage in errorMessage

    def LoginLocked(self,expectedErrorMessage):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.errorMessage)
        )
        errorMessage = element.text
        print(errorMessage)
        print("done")
        assert expectedErrorMessage in errorMessage






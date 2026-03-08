import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_Pages.BasePage import BasePage


class DeliveryAddressPage(BasePage):

    def __init__(self,driver):
        print("User Delivery Address Page")
        super().__init__(driver)
        self.firstName = (By.ID, "first-name")
        self.lastName = (By.ID, "last-name")
        self.postalCode = (By.ID, "postal-code")
        self.continueButton = (By.ID, "continue")

    def fillInDeliveryAddress(self,firstname,lastname,postalcode):
        self.driver.find_element(*self.firstName).send_keys(firstname)
        self.driver.find_element(*self.lastName).send_keys(lastname)
        self.driver.find_element(*self.postalCode).send_keys(postalcode)
        self.driver.find_element(*self.continueButton).click()


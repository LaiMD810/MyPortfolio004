from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_Pages.BasePage import BasePage


class CompletePage(BasePage):
    def __init__(self,driver):
        print("Completed Acknowledgment Page")
        super().__init__(driver)
        self.completeTitleMessage = (By.CSS_SELECTOR, ".complete-header")
        self.completeMessage = (By.CSS_SELECTOR, ".complete-text")
        print("Complete Page")

    def verifyCompleteMessage(self):
        completeTitleMessage = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.completeTitleMessage)).text
        completeMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.completeMessage)).text
        print(completeTitleMessage)
        assert "Thank you for your order!" in completeTitleMessage
        print(completeMessage)
        assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in completeMessage

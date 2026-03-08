from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_Pages.BasePage import BasePage


class CheckOutPage(BasePage):
    def __init__(self,driver):
        print("Checkout  Page")
        super().__init__(driver)
        self.CheckoutProductList = (By.XPATH, "//div[@class='cart_item']")
        self.CheckoutProduct = (By.XPATH, ".//div[contains(@class,'inventory_item_name')]")
        self.subTotalprice = (By.CSS_SELECTOR, ".summary_subtotal_label")
        self.finalTotalPrice = (By.CSS_SELECTOR, ".summary_total_label")
        self.finishButton = (By.ID, "finish")


    def verifyCheckoutProductList(self):
        CheckoutProductList = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.CheckoutProductList)
        )
        for CheckoutProduct in CheckoutProductList:
            product = CheckoutProduct.find_element(*self.CheckoutProduct)
            print(product.text)

    def verifyPrices(self,subtotal,finaltotal):
        subTotalPrice = self.driver.find_element(*self.subTotalprice)
        finalTotalPrice = self.driver.find_element(*self.finalTotalPrice)
        print(subTotalPrice.text)
        print(finalTotalPrice.text)
        assert subtotal in subTotalPrice.text
        assert finaltotal in finalTotalPrice.text

    def clickFinishButton(self):
        self.driver.find_element(*self.finishButton).click()


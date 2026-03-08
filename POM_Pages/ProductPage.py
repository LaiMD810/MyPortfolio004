from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_Pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.productList  = (By.XPATH,"//div[@class='inventory_item']")
        self.productName = (By.XPATH,".//div[contains(@class,'inventory_item_name')]")
        self.AddtoCart = (By.XPATH, ".//button[contains(@class,'btn_inventory')]")
        self.cartButton = (By.ID,"shopping_cart_container")

    def clickCartButton(self):
        cart = self.driver.find_element(*self.cartButton)
        cart.click()

    def addProducts(self,selected_products):
        #productList = self.driver.find_elements(*self.productList)
        productList = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.productList)
        )
        for products in productList:
            product = products.find_element(*self.productName).text

            if product in selected_products:
                products.find_element(*self.AddtoCart).click()


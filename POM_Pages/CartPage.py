from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_Pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.cartList  = (By.XPATH,"//div[@class='cart_item']")
        self.productinCart = (By.XPATH,".//div[contains(@class,'inventory_item_name')]")
        self.checkOutButton = (By.ID,"checkout")

    def clickCheckOutButton(self):
        cart = self.driver.find_element(*self.checkOutButton)
        cart.click()

    def verifyProductsInCart(self,expected_product):
        cartItem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.cartList)
        )
        cart_list = []

        for item in cartItem:
            product = item.find_element(*self.productinCart)
            cart_list.append(product.text)
            print(cart_list[0])

        for product in expected_product:
            assert product in cart_list



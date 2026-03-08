import time
import json
import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

from POM_Pages.CompletePage import CompletePage
from POM_Pages.LoginPage import LoginPage
from POM_Pages.ProductPage import ProductPage
from POM_Pages.CartPage import CartPage
from POM_Pages.DeliveryAddressPage import DeliveryAddressPage
from POM_Pages.CheckoutPage import CheckOutPage

producttestdatapath ='../TestData/ProductTestData.json'
with open(producttestdatapath) as file:
    product_test_data = json.load(file)["ProductData"]

@pytest.mark.parametrize("test_data",product_test_data)
def test_purchaseProduct(driverBrowser,test_data): #using the json test data, and run the test in firefox and chrome browser
    driver = driverBrowser
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Perform Login
    loginPage = LoginPage(driver)
    loginPage.Login("standard_user", "secret_sauce")

    # product_to_be_selected =Variable for selecting products at the Product page and verify the selected products at the cart page
    productPage = ProductPage(driver)
    productPage.addProducts(test_data["productTobeSelected"])
    productPage.clickCartButton()

    cartPage = CartPage(driver)
    cartPage.verifyProductsInCart(test_data["productTobeSelected"])
    cartPage.clickCheckOutButton()

    # Page for entering the delivery address
    deliveryPage = DeliveryAddressPage(driver)
    deliveryPage.fillInDeliveryAddress("Hello", "world", "676767")

    # CheckOut Page
    checkoutPage = CheckOutPage(driver)
    checkoutPage.verifyCheckoutProductList()
    checkoutPage.verifyPrices(
        test_data["expectedPricebeforeTax"],
        test_data["expectedPriceAfterTax"]
    )
    checkoutPage.clickFinishButton()

    # Product Ordered Acknowledgment page
    completePage = CompletePage(driver)
    completePage.verifyCompleteMessage()



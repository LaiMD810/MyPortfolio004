# Selenium Python Automation Portfolio

This project is a simple UI automation framework built with **Python, Selenium, and Pytest** using the **Page Object Model (POM)** design pattern.

The goal of this project is to demonstrate a basic automation testing structure that separates test logic, page objects, and test data.

---

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* JSON Test Data

---

## Project Structure

```
MyPortfolio004
│
├── POM_Pages
│   ├── BasePage.py
│   ├── LoginPage.py
│   ├── ProductPage.py
│   ├── CartPage.py
│   ├── CheckoutPage.py
│   ├── DeliveryAddressPage.py
│   └── CompletePage.py
│
├── tests
│   ├── conftest.py
│   ├── test_login.py
│   └── test_purchase_product.py
│
├── TestData
│   ├── LoginTestData.json
│   └── ProductTestData.json

```

---

## Test Scenarios Covered

* User login
* Add product to cart till Checkout and complete purchase flow

---

## Demo
test_login.py - Total 6 Test Cases ->  3 Test Cases Run on FireFox browser & 3 Test Cases Run on Chrome browser
<img width="1857" height="941" alt="test_login_result" src="https://github.com/user-attachments/assets/2c812149-6e59-46c3-bafb-ba329ba9a618" />
https://github.com/user-attachments/assets/069e95cc-841b-4565-8000-bab7d4a7f6b8



test_purchase_product.py - Total 4 Test Cases ->  2 Test Cases Run on Firefox browser & 2 Test Cases Run on Chrome browser (Expected to Have Failed  Test Cases)
<img width="1910" height="615" alt="test_PurchaseProduct_result" src="https://github.com/user-attachments/assets/7c78021d-b369-4143-8c47-3372b363e564" />
https://github.com/user-attachments/assets/daf5c623-dbc0-4d98-ac52-874cd9d71754


This project is created as part of my QA automation practice and portfolio.
The framework demonstrates a basic structure that can be extended with more test cases and with the Generate Report

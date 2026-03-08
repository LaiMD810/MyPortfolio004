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


This project is created as part of my QA automation practice and portfolio.
The framework demonstrates a basic structure that can be extended with more test cases and utilities.

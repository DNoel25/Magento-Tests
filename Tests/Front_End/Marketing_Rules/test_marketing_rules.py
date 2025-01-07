import time

import pytest
from selenium import webdriver
from Pages.Front_End.Marketing_Rules.marketing_rules_page import MarketingRules
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://uatnew.bonz.com/en")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_toverify_home_page(driver):
    print(" ")
    print("Test the home page..")
    # Verify URL
    current_url = driver.current_url
    assert current_url == "https://uatnew.bonz.com/en", f"URL mismatch: {current_url}"
    print("Redirection successful. Redirected to:", current_url)

def test_catelog_price(driver):
    guest = MarketingRules(driver)
    guest.redirect_to_home_page()
    guest.redirect_to_product_page()
    guest.check_catelog_price_discout()

def test_cart_price_without_coupon(driver):
    guest = MarketingRules(driver)
    guest.add_to_cart()
    guest.go_to_cart()
    guest.check_price_without_coupon()




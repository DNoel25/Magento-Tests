import pytest
from selenium import webdriver
from Pages.Front_End.logged_user_page import LoggedInUser
import time
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Adjust as per your browser
    driver.maximize_window()
    yield driver
    driver.quit()

def test_logged_in_user_flow(driver):
    logged_in = LoggedInUser(driver)
    logged_in.redirect_to_login_page()
    logged_in.login_successfully("d.noel251299@gmail.com", "Welcome@123")  # Replace with test credentials
    logged_in.go_to_home_page()

def test_logged_in_order_process(driver):
    logged_in = LoggedInUser(driver)
    logged_in.go_to_category_page()
    # logged_in.verify_products_available()
    logged_in.go_to_product_page()
    logged_in.add_to_cart()
    logged_in.go_to_cart()
    logged_in.go_to_shipping()
    time.sleep(2)

    if logged_in.is_savedaddress_there():
        logged_in.add_new_address()
    else:
        logged_in.fill_the_shipping_details()
    logged_in.fill_the_payement()
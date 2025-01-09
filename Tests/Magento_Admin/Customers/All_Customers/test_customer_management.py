from wsgiref.types import WSGIEnvironment

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Magento_Admin.Customers.All_Customers.customer_management_page import CustomerManagement
import time
from selenium.webdriver.chrome.service import Service
from Pages.sidebar_page import SideNavigationPage

@pytest.fixture(scope="module")
def driver():
    driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://uatnew.bonz.com/BonzGroupAdmin/admin/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_logged_in_user_flow(driver):
    magento = CustomerManagement(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_dashboard_page()

def test_redirection_to_customers(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_customers_menu()
    side_nav.open_all_customers()
    time.sleep(2)

def test_redirection_to_new_customers(driver):
    magento = CustomerManagement(driver)
    magento.nav_to_new_customer()
    time.sleep(3)

#fill the details
def test_fill_mandatory(driver):
    print(" ")
    print("Filling the empty fields..")
    magento = CustomerManagement(driver)
    magento.fill_mandatory_fields("NoelAutomation", "DurairajAutomation","d.noel251299@gmail.com")
    # magento.save_product_simple()
    time.sleep(5)

def test_save_customer(driver):
    print(" ")
    print("Test the save customer button..")
    magento = CustomerManagement(driver)
    magento.click_save_btn()



#
# def test_payment_or_shipping_method(driver):
#     print(" ")
#     print("Selecting the payment method and shipping method..")
#     magento = CustomerManagement(driver)
#     magento.selecting_payment_or_shipping()
#
# def test_submit_order(driver):
#     print(" ")
#     print("Submitting the order..")
#     magento = CustomerManagement(driver)
#     magento.submit_order()
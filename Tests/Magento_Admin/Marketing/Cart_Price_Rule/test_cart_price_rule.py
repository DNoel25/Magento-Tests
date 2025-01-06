from wsgiref.types import WSGIEnvironment
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Magento_Admin.Marketing.Cart_Price_Rule.cart_price_rule_page import CartPriceRuleManagement
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
    magento = CartPriceRuleManagement(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_home_page()

def test_redirection_to_cart_price_rule(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_marketing_menu()
    side_nav.open_cart_price_rule_menu()
    time.sleep(2)

def test_redirection_to_new_cart_price_rule(driver):
    magento = CartPriceRuleManagement(driver)
    magento.nav_to_new_cart_price_rule()
    time.sleep(3)

#fill the details
def test_add_new(driver):
    print(" ")
    print("Filling the required fields..")
    magento = CartPriceRuleManagement(driver)
    magento.fill_mandatory_fields("testAutomationCartRuleWithCoupon", "50", "TestAutomationSimple", True, coupon_name="SpecialCoupon")
    magento.click_save_btn()
    print("Successfully created the cart price rule WITH coupon")
    time.sleep(5)
    magento.nav_to_new_cart_price_rule()
    time.sleep(2)
    magento.fill_mandatory_fields("testAutomationCartRuleWithoutCoupon", "50", "TestAutomationSimple", False)
    magento.click_save_btn()
    print("Successfully created the cart price rule WITHOUT coupon")
    time.sleep(2)


# def test_save_customer(driver):
#     print(" ")
#     print("Test the save customer button..")
#     magento = CartPriceRuleManagement(driver)
#     magento.click_save_btn()
#


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
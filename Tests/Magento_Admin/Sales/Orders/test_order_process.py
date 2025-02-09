import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Magento_Admin.Sales.Orders.order_process_page import OrderProcess
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
    magento = OrderProcess(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_home_page()

def test_redirection_to_orders(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_sales_menu()
    side_nav.open_orders()
    time.sleep(2)

def test_redirection_to_new_orders(driver):
    magento = OrderProcess(driver)
    magento.nav_to_new_order("d.noel251299@gmail.com")

def test_add_product(driver):
    print(" ")
    print("Adding a product to the order..")
    magento = OrderProcess(driver)
    magento.add_products("testAutomationSimple")

    #fill the details
def test_fill_mandatory(driver):
    print(" ")
    print("Filling the empty fields..")
    magento = OrderProcess(driver)
    magento.fill_mandatory_fields("NoelAutomation", "DurairajAutomation","testAddressAutomation", "testCityAutomation", "testZipAutomation", "testPNumberAutomation" )
    # magento.save_product_simple()
    time.sleep(5)

def test_payment_or_shipping_method(driver):
    print(" ")
    print("Selecting the payment method and shipping method..")
    magento = OrderProcess(driver)
    magento.selecting_payment_or_shipping()

def test_submit_order(driver):
    print(" ")
    print("Submitting the order..")
    magento = OrderProcess(driver)
    magento.submit_order()

#Starting the post order testing

def test_invoicing(driver):
    print(" ")
    print("Invoicing the order..")
    magento = OrderProcess(driver)
    magento.go_to_invoice()
    magento.submit_invoice()
    time.sleep(5)

def test_shipping(driver):
    print(" ")
    print("Shipping the order..")
    magento = OrderProcess(driver)
    magento.go_to_ship()
    magento.submit_shipping()
    time.sleep(5)


def test_creditmemo(driver):
    print(" ")
    print("Testing credit memo for the order..")
    magento = OrderProcess(driver)
    magento.go_to_creditmemo()
    magento.submit_creditmemo()
    time.sleep(5)

def test_re_order(driver):
    print(" ")
    print("Testing re order..")
    magento = OrderProcess(driver)
    magento.make_re_order()
    time.sleep(5)







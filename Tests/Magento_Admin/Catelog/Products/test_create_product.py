import pytest
from selenium import webdriver
from Pages.Magento_Admin.Catelog.Products.create_product_page import CreateProducts
import time
from selenium.webdriver.chrome.service import Service

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
    magento = CreateProducts(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    magento.go_to_home_page()

# def test_logged_in_order_process(driver):
#     logged_in = LoggedInUser(driver)
#     logged_in.go_to_category_page()
#     # logged_in.verify_products_available()
#     logged_in.go_to_product_page()
#     logged_in.add_to_cart()
#     logged_in.go_to_cart()
#     logged_in.go_to_shipping()
#     time.sleep(2)
#
#     if logged_in.is_savedaddress_there():
#         logged_in.add_new_address()
#     else:
#         logged_in.fill_the_shipping_details()
#     logged_in.fill_the_payement()
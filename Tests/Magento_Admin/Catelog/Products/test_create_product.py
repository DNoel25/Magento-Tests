import pytest
from selenium import webdriver
from Pages.Magento_Admin.Catelog.Products.create_product_page import CreateProducts
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
    magento = CreateProducts(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_home_page()

def test_redirection_to_products(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_catelog_menu()
    side_nav.open_products()
    time.sleep(2)

def test_simple_product(driver):
    magento = CreateProducts(driver)
    magento.nav_to_addnew_simple_product()

    #fill the details
    magento.fill_mandatory_fields_simple("testAutomationSimple", "testAutomationSimple","222", "5" )
    magento.save_product_simple()
    time.sleep(5)

def test_config_product(driver):
    magento = CreateProducts(driver)
    magento.nav_to_addnew_config_product()
    magento.fill_configurable_product_fields("testAutomationConfig", "testAutomationConfig", "999")
    magento.add_configurations(
        attributes=["93", "173"],  # Replace with actual attributes
        attribute_values={
            "size": ["XL", "L", "XS"],
            "color": ["Red", "Blue", "Green"]
        }
    )
    magento.save_product_config()



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



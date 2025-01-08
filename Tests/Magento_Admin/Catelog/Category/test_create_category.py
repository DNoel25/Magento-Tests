import pytest
from selenium import webdriver
from Pages.Magento_Admin.Catelog.Category.create_category_page import CreateCatagory
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
    magento = CreateCatagory(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_home_page()

def test_redirection_to_category(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_catelog_menu()
    side_nav.open_category()
    time.sleep(2)

def test_sub_category(driver):
    magento = CreateCatagory(driver)
    magento.nav_to_addnew_sub_category()


    # fill the details
    magento.fill_mandatory_fields_simple( "testAutomationCategory")
    # add products to the category
    magento.add_products_to_category("testAutomationSimple")
    magento.save_category()






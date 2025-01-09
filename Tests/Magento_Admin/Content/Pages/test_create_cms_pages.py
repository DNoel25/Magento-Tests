import pytest
from selenium import webdriver
from Pages.Magento_Admin.Content.Pages.create_cms_pages_page import CreateCMS
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
    magento = CreateCMS(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_home_page()

def test_redirection_to_cmspages(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_content_menu()
    side_nav.open_cmspages_menu()
    time.sleep(2)

def test_nav_to_add(driver):
    magento = CreateCMS(driver)
    result = magento.nav_to_add_new()
    assert result is True, "Failed to navigate to the 'ADD NEW' form page"
    time.sleep(2)

def test_the_enable(driver):
    magento = CreateCMS(driver)
    result = magento.check_enable_toggle()
    assert result is True, "Failed to enable the toggle."

def test_fill_mandatory(driver):
    magento = CreateCMS(driver)
    magento.fill_mandatory_fields("TestAutomationCMSPageByNoel")

def test_fill_content(driver):
    magento = CreateCMS(driver)
    content_heading = "TestAutomationCMSPage_Content_Heading"
    content = "TestAutomation is the automated content by Noel Durairaj"
    magento.fill_content(content_heading, content)

def test_save(driver):
    magento = CreateCMS(driver)
    magento.save()



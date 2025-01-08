import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Pages.Front_End.user_registration_page  import UserRegistration

@pytest.fixture(scope="module")
def driver():
    driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://uatnew.bonz.com/en/customer/account/create/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_verify_registrationpage(driver):
    print("Redirecting to the registration page and starting the testing..")
    user_reg = UserRegistration(driver)
    user_reg.confirm_the_page()

def test_filling_fields(driver):
    print("")
    print("Filling all the mandatory fields")
    user_reg = UserRegistration(driver)

    first_n = "testAutomationByNoel"
    last_n = "testAutomationByNoel"
    email = "noel.durairaj@neosolax.com"
    pwd = "Welcome@123"
    c_pwd = "Welcome@123"

    user_reg.filling_mandatory_fields(first_n, last_n, email, pwd, c_pwd)


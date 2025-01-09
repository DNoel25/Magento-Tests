import time
from telnetlib import EC

from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerManagement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def redirect_to_login_page(self):
        self.driver.get("https://uatnew.bonz.com/BonzGroupAdmin/admin/")

    def login_successfully(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)  # Adjust selector
        self.driver.find_element(By.ID, "login").send_keys(password)
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'action-login') and contains(@class, 'action-primary')]"))
        )
        signin.click()

    def test_dashboard_page(self):
        homepage = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title' and text()='Dashboard']"))
        )
        print("Successfully redirected to the dashboard")

    # Method to close modals
    def close_notifications(self):
        try:

            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-inner-wrap"))
            )
            close_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-role='closeBtn']")
            close_button.click()
            print("Blocking nofitifications closed.")
        except TimeoutException:
            print("No blocking notifications appeared.")


    def nav_to_new_customer(self):
        create_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add" and @title="Add New Customer"]'))
        )
        create_order.click()
        print("Successfully redirected to new customer creation form")

    def add_products(self, sku):

        time.sleep(2)
        try:
            add_product = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'add_products'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_product)
            add_product.click()
            time.sleep(2)

            sku_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'sales_order_create_search_grid_filter_sku'))
            )
            sku_element.clear()
            sku_element.send_keys(sku)
            sku_element.send_keys(Keys.RETURN)
            time.sleep(2)

            checkbox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'id_4672'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", checkbox)
            checkbox.click()
            time.sleep(2)

            add_selected = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@title="Add Selected Product(s) to Order" and contains(@class, "action-add")]'))
            )
            # self.driver.execute_script("window.scrollBy(0, 0);")
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_selected)
            add_selected.click()
            time.sleep(2)
        except TimeoutException:
            print("Can not find the elements")
        except ElementClickInterceptedException:
            print("An element is giving overlay to the clickable element")

    # Locators
    FIRST_NAME = (By.NAME, "customer[firstname]")  # Replace with actual locator
    LAST_NAME = (By.NAME, "customer[lastname]")  # Replace with actual locator
    EMAIL = (By.NAME, "customer[email]")  # Replace with actual locator

    def fill_if_empty(self, locator, value, field_name):
        element = self.wait.until(EC.presence_of_element_located(locator))
        if element.get_attribute("value").strip() == "":
            element.clear()
            element.send_keys(value)
        else:
            print(f"{field_name} is already filled with the value.")

    def fill_mandatory_fields(self, first_name, last_name, email):

        self.fill_if_empty(self.FIRST_NAME, first_name, "first_name")
        self.fill_if_empty(self.LAST_NAME, last_name, "last_name")
        self.fill_if_empty(self.EMAIL, email, "email")
        time.sleep(4)

    def click_save_btn(self):
        try:
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="save"]'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", save_button)
            save_button.click()
            print("Successfully created the customer")
            time.sleep(5)

        except TimeoutException:
            print("No save button is found!")
        except InvalidSelectorException:
            print("Invalid selector")
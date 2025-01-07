import time

from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatelogManagement:
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

    def test_home_page(self):
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


    def nav_to_new_catelog_price_rule(self):
        create_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add" and @title="Add New Rule"]'))
        )
        create_order.click()
        print("Successfully redirected to new catelog price rule creation form")


    # Locators
    RULE_NAME = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div[2]/fieldset/div[2]/div[2]/input")
    ACTIVE = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div[2]/fieldset/div[4]/div[2]/div/label")
    WEBSITES = (By.NAME, "website_ids")  # Replace with actual locator
    CUSTOMER_GROUPS = (By.NAME, "customer_group_ids")  # Replace with actual locator

    def fill_mandatory_fields(self, rule_name, percentage):

        self.driver.find_element(*self.RULE_NAME).send_keys(rule_name)
        self.driver.find_element(*self.ACTIVE).click()

        # Wait for the WEBSITES element to be visible
        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.WEBSITES)
        )
        # Create a Select object
        select = Select(select_element)
        # Select all options
        for option in select.options:
            select.select_by_value(option.get_attribute("value"))

        time.sleep(1)

        # Wait for the CUSTOMER GROUPS element to be visible
        select_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CUSTOMER_GROUPS)
        )
        # Create a Select object
        select = Select(select_element)
        # Select all options
        for option in select.options:
            select.select_by_value(option.get_attribute("value"))

        time.sleep(1)

        action = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(@class, 'admin__collapsible-title') and span[@data-bind=\"i18n: label\" and text()='Actions']]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", action)
        action.click()

        discount_amount = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "discount_amount"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", action)
        discount_amount.clear()
        discount_amount.send_keys(percentage)

        save_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "save"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", save_btn)
        save_btn.click()


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
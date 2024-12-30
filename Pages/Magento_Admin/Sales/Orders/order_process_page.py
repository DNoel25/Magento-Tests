import time

from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderProcess:
    def __init__(self, driver):
        self.driver = driver

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

# Creating a simple product
    def nav_to_addnew_simple_product(self):
        # Click the arrow or button to open the dropdown
        arrow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add_new_product"]/button[2]'))
        )
        arrow.click()

        try:
            # Wait for the dropdown menu to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu"))
            )
            # Click the "Simple Product" option
            simple_product_option = self.driver.find_element(By.XPATH, "//span[@title='Simple Product']")
            simple_product_option.click()
            print("Selected 'Simple Product'.")
        except Exception as e:
            print(f"Error selecting 'Simple Product': {e}")

    # Method to fill mandatory fields
    def fill_mandatory_fields_simple(self, product_name, sku, price, quantity):
        try:
            # Wait for and fill 'Product Name'
            product_name_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[name]']"))
            )
            product_name_field.clear()
            product_name_field.send_keys(product_name)

            # Fill 'SKU'
            sku_field = self.driver.find_element(*(By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[sku]']"))
            sku_field.clear()
            sku_field.send_keys(sku)

            # Fill 'Price'
            price_field = self.driver.find_element(*(By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[price]']"))
            price_field.clear()
            price_field.send_keys(price)

            # Fill 'Quantity'
            quantity_field = self.driver.find_element(*(By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[quantity_and_stock_status][qty]']"))
            quantity_field.clear()
            quantity_field.send_keys(quantity)

            print("Mandatory fields filled successfully.")
        except Exception as e:
            print(f"Error while filling mandatory fields: {e}")

    # Method to save the product
    def save_product_simple(self):
        try:
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-ui-id='save-button']"))
            )
            save_button.click()
            print("Product saved successfully.")
            back = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='back']"))
            )
            back.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error while saving the product: {e}")

#Creating a configurable product
    def nav_to_addnew_config_product(self):
        # Click the arrow or button to open the dropdown
        arrow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add_new_product"]/button[2]'))
        )
        arrow.click()

        try:
            # Wait for the dropdown menu to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu"))
            )
            # Click the "Simple Product" option
            simple_product_option = self.driver.find_element(By.XPATH, "//span[@title='Configurable Product']")
            simple_product_option.click()
            print("Selected 'Configurable Product'.")
        except Exception as e:
            print(f"Error selecting 'Configurable Product': {e}")

    # Method to fill mandatory fields
    def fill_configurable_product_fields(self, product_name, sku, price):
        try:
            # Wait for and fill 'Product Name'
            product_name_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[name]']"))
            )
            product_name_field.clear()
            product_name_field.send_keys(product_name)

            # Fill 'SKU'
            sku_field = self.driver.find_element(*(By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[sku]']"))
            sku_field.clear()
            sku_field.send_keys(sku)

            # Fill 'Price'
            price_field = self.driver.find_element(*(By.XPATH, "//input[@type='text' and @class='admin__control-text' and @name='product[price]']"))
            price_field.clear()
            price_field.send_keys(price)

            print("Configurable product fields filled successfully.")
        except Exception as e:
            print(f"Error while filling configurable product fields: {e}")

    def add_configurations(self, attributes, attribute_values):
        try:
            # Click 'Add Configurations' button
            add_config_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="container"]/div/div[2]/div[4]/div[2]/fieldset/div[1]/div[1]/button/span'))
            )
            self.driver.execute_script("arguments[0].click();", add_config_button)
            print("Clicked on 'Add Configurations' button.")

            # Scroll to ensure elements are in view
            self.driver.execute_script("window.scrollBy(0, 500);")

            # Select attributes
            for attribute in attributes:
                try:
                    print(f"Attempting to select attribute: {attribute}")
                    attribute_checkbox = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, f"//input[@type='checkbox' and @value='{attribute}']"))
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", attribute_checkbox)
                    if not attribute_checkbox.is_selected():
                        attribute_checkbox.click()
                    print(f"Selected attribute: {attribute}")
                    time.sleep(2)
                except Exception as e:
                    print(f"Failed to select attribute {attribute}: {e}")
                    continue

            # Click 'Next'
            next_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//button[@class="action-default action-primary action-next-step"]'))
            )
            next_button.click()
            print("Clicked on 'Next'.")

            # Fill attribute values
            for attribute, values in attribute_values.items():
                for value in values:
                    try:
                        print(f"Attempting to select value: {value}")
                        # Update XPath to use data-attribute-option-title
                        value_checkbox = WebDriverWait(self.driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH, f"//li[@data-attribute-option-title='{value}']"))
                        )
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", value_checkbox)
                        # Click the checkbox only if it's not already selected
                        if not value_checkbox.is_selected():
                            value_checkbox.click()
                            print(f"Selected value: {value}")
                        else:
                            print(f"Value {value} is already selected.")
                    except Exception as e:
                        print(f"Error selecting value {value}: {e}")

            # Click 'Next' again
            next_button.click()
            print("Clicked 'Next' again.")

            # Click 'Next' again
            next_button.click()
            print("Clicked 'Next' again.")


            gen_product = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/aside[14]/div[2]/div/div/div/div/div[2]/div/div[3]/button"))
            )

            time.sleep(2)
            # Click 'Next' again
            gen_product.click()
            print("Clicked 'Generate Products'.")

            print("Configurations added successfully.")
        except Exception as e:
            print(f"Error while adding configurations: {e}")

    # Method to save the product
    def save_product_config(self):
        print("1")
        time.sleep(4)
        try:
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='save-button' and @title='Save']"))
            )
            save_button.click()
            time.sleep(5)
            print("Product saved successfully.")
        except Exception as e:
            print(f"Error while saving the product: {e}")

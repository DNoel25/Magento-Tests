import time

from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateCatagory:
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
    def nav_to_addnew_sub_category(self):

        add_subcategory = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add_subcategory_button"]'))
        )
        add_subcategory.click()
        print("Add new sub category button is clicked successfully and redirecting to the add new form..")
        time.sleep(10)

    # Method to fill mandatory fields
    def fill_mandatory_fields_simple(self, category_name):

        try:
            active = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(@class, 'admin__actions-switch-label')]"))
            )

            # Check if the toggle bar is already enabled
            if active.get_attribute("value") == "0":  # Assuming '0' means inactive
                active.click()  # Activate the toggle bar
                print("The category is enabled.")
            else:
                print("The category is already enabled.")
        except Exception as e:
            print(f"Error with category enable toggle selection: {e}")

        # Locate the input field related to the category name
        try:
            category_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and contains(@class, 'admin__control-text')]"))
            )
            print("Category input field is visible and clickable.")

            # Scroll into view to ensure visibility
            self.driver.execute_script("arguments[0].scrollIntoView(true);", category_input)
            print("Scrolled to the category input field.")

            # Clear the field
            category_input.clear()

            # Enter the new category name
            category_input.send_keys(category_name)

            # Validate the value entered
            actual_value = category_input.get_attribute("value")
            if actual_value == category_name:
                print("Category name set successfully!")
            else:
                print(f"Category name mismatch! Expected: {category_name}, Found: {actual_value}")

        except Exception as e:
            print(f"Error interacting with category input field: {e}")


    def add_products_to_category(self, search_sku):
        # Go to the adding products to the category section
        products_in_category = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//span[text()='Products in Category']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                   products_in_category)
        products_in_category.click()
        time.sleep(4)

        sku_textfield = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "catalog_category_products_filter_sku"))
        )
        sku_textfield.clear()
        sku_textfield.send_keys(search_sku)
        time.sleep(2)

        first_row_locator = (By.CSS_SELECTOR, "table tbody tr:first-child")
        # Wait for the first row to be clickable and click it
        first_row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(first_row_locator)
        )
        first_row.click()
        time.sleep(5)
        print("Successfully selected the product from the table")

    # Method to save the product
    def save_category(self):
        try:
            save_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='save']"))
            )
            save_button.click()
            print("Category saved successfully.")
            time.sleep(5)

        except Exception as e:
            print(f"Error while saving the category: {e}")



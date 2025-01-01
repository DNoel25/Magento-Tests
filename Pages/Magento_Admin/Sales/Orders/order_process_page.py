import time
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderProcess:
    def __init__(self, driver):
        # self.wait = None
        # self.driver = driver
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

# Placing an order
    def nav_to_new_order(self, email):
        create_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add" and @title="Create New Order"]'))
        )
        create_order.click()
        print("Successfully redirected to new orders form")

        print("Selecting the customer..")
        search_in_email = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sales_order_create_customer_grid_filter_email" and @data-ui-id="widget-grid-column-filter-text-2-filter-email"]'))
        )
        search_in_email.clear()
        search_in_email.send_keys(email)

        first_row_locator = (By.CSS_SELECTOR, "table tbody tr:first-child")
        # Wait for the first row to be clickable and click it
        first_row = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(first_row_locator)
        )
        first_row.click()
        time.sleep(5)
        print("Successfully selected the current user by email")

        print("Selecting the store view..")
        store_view = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="store_1" and @class="admin__control-radio"]'))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", store_view)

        store_view.click()

        print("Successfully redirected to add new order form..")

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
    FIRST_NAME = (By.ID, "order-billing_address_firstname")  # Replace with actual locator
    LAST_NAME = (By.ID, "order-billing_address_lastname")  # Replace with actual locator
    STREET_ADDRESS = (By.ID, "order-billing_address_street0")  # Replace with actual locator
    # COUNTRY = (By.ID, "country")  # Replace with actual locator
    CITY = (By.ID, "order-billing_address_city")  # Replace with actual locator
    ZIP_CODE = (By.ID, "order-billing_address_postcode")  # Replace with actual locator
    PHONE_NUMBER = (By.ID, "order-billing_address_telephone")  # Replace with actual locator

    def fill_if_empty(self, locator, value, field_name):
        element = self.wait.until(EC.presence_of_element_located(locator))
        if element.get_attribute("value").strip() == "":
            element.clear()
            element.send_keys(value)
        else:
            print(f"{field_name} is already filled with the value.")

    def fill_mandatory_fields(self, first_name, last_name, street_address, city, zip_code, phone_number):

        self.fill_if_empty(self.FIRST_NAME, first_name, "first_name")
        self.fill_if_empty(self.LAST_NAME, last_name, "last_name")
        self.fill_if_empty(self.STREET_ADDRESS, street_address, "street_address")
        self.fill_if_empty(self.CITY, city, "city")
        self.fill_if_empty(self.ZIP_CODE, zip_code, "zip_code")
        self.fill_if_empty(self.PHONE_NUMBER, phone_number, "phone_number")
        time.sleep(4)

    def selecting_payment_or_shipping(self):
        """
                Select the 'Cash on Delivery' payment method if not already selected.
        """
        print("Locating the payment method section...")
        self.wait.until(EC.presence_of_element_located((By.ID, "order-billing_method")))

        print("Checking 'Cash on Delivery' payment method...")
        cod_radio_button = self.wait.until(EC.presence_of_element_located((By.ID, "p_method_cashondelivery")))

        if cod_radio_button.get_attribute("checked") == "true":
            print("'Cash on Delivery' is already selected.")
        else:
            print("Selecting 'Cash on Delivery' payment method...")
            # Click the label to select the payment method
            self.driver.find_element(*By.XPATH, "//label[@for='p_method_cashondelivery']").click()
            print("'Cash on Delivery' has been selected.")

        """
                Click the 'Get Shipping Methods and Rates' link.
        """
        print("Clicking the 'Get Shipping Methods and Rates' link...")
        get_shipping_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='action-default']/span[text()='Get shipping methods and rates']")))
        get_shipping_link.click()

        """
                Select the first available shipping method.
        """
        print("Selecting the first available shipping method...")
        shipping_option = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @name='order[shipping_method]']")))
        shipping_option.click()
        label = self.driver.find_element(*(By.XPATH, "//input[@type='radio' and @name='order[shipping_method]']/following-sibling::label"))
        print(f"Selected shipping method: {label.text.strip()}")

    #Method to save the product
    def submit_order(self):
        try:
            # Wait for the loading mask to disappear
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loading-mask"))
            )

            # Wait for the submit button to be clickable
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@id='submit_order_top_button' and @title='Submit Order']"))
            )

            # Scroll to the button (if necessary)
            self.driver.execute_script("window.scrollBy(0, 0);")

            # Click the submit button
            submit_button.click()
            print("Submitted the order successfully.")
            time.sleep(2)
        except Exception as e:
            print(f"Error while submitting the order: {e}")
#
    def go_to_invoice(self):
        try:
            invoice = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'order_invoice'))
            )
            invoice.click()
        except Exception as e:
            print(f"Error while submitting the invoice: {e}")

    def submit_invoice(self):
        try:
            submit_invoice = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@title="Submit Invoice" and @class="action-default scalable save submit-button primary"]'))
            )

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",submit_invoice)

            submit_invoice.click()
            print("Submitted the invoice successfully.")
            time.sleep(3)
        except Exception as e:
            print(f"Error while submitting the invoice: {e}")


    def go_to_ship(self):
        try:
            invoice = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'order_ship'))
            )
            invoice.click()
        except Exception as e:
            print(f"Error while submitting the shipping: {e}")

    def submit_shipping(self):
        try:
            submit_shipment = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@title="Submit Shipment" and @class="action-default scalable save submit-button primary"]'))
            )

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",submit_shipment)

            submit_shipment.click()
            print("Submitted the shipment successfully.")
            time.sleep(3)
        except Exception as e:
            print(f"Error while submitting the shipment: {e}")

    def go_to_creditmemo(self):
        try:
            invoice = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'order_creditmemo'))
            )
            invoice.click()
        except Exception as e:
            print(f"Error while submitting the credit memo: {e}")

    def submit_creditmemo(self):
        try:
            submit_creditmemo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@title="Refund Offline" and @class="action-default scalable save submit-button primary"]'))
            )

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",submit_creditmemo)

            submit_creditmemo.click()
            print("Submitted the credit memo successfully.")
            time.sleep(3)
        except Exception as e:
            print(f"Error while submitting the credit memo: {e}")

    def make_re_order(self):
        try:
            invoice = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'order_reorder'))
            )
            invoice.click()
            self.submit_order()
            print("Re order successfully.")
        except Exception as e:
            print(f"Error while submitting the order reorder: {e}")


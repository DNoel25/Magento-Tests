import time
from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoggedInUser:
    def __init__(self, driver):
        self.driver = driver

    def redirect_to_login_page(self):
        self.driver.get("https://uatnew.bonz.com/en/customer/account/login")

    def login_successfully(self, username, password):
        self.driver.find_element(By.ID, "email").send_keys(username)  # Adjust selector
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)
        self.driver.find_element(By.ID, "send2").click()  # Adjust selector

    def go_to_home_page(self):
        self.driver.get("https://uatnew.bonz.com/en")

    def go_to_category_page(self):
        # Wait for the category link to be visible before clicking
        category_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='custom-nav__link' and @href='https://uatnew.bonz.com/en/men']"))  # Adjust XPath
        )
        category_link.click()
        time.sleep(2)

    def verify_products_available(self):
        # Wait for the products to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item"))  # Adjust selector
        )
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product-item")  # Adjust selector
        assert len(products) > 0, "No products available"

        # Wait for the product list container to be visible
        product_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//ol[@class='products list items product-items']"))
        )

        # Now, check if there are at least one product item in the list
        product_items = product_list.find_elements(By.XPATH, ".//li[contains(@class, 'product-item')]")

        if len(product_items) > 0:
            print("At least one product is present in the category.")
            return product_items  # Return the list of product items
        else:
            print("No products found in the category.")
            return []  # Return an empty list if no products are found

    def go_to_product_page(self):
        try:
            # Scroll the page slightly to ensure product items are loaded
            self.driver.execute_script("window.scrollBy(0, 200);")

            # Wait for the products container to load and verify products are available
            product_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))
            )

            if len(product_items) > 0:
                # Find the first product link using CSS selector
                first_product_link = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item:first-child a.product-item-link"))
                )

                # Scroll the element into view before clicking
                self.driver.execute_script("arguments[0].scrollIntoView();", first_product_link)

                # Click the first product link
                first_product_link.click()
                time.sleep(3)  # Optional delay for verification
                print("First product link is clicked successfully")
            else:
                print("No products available on the page")
        except Exception as e:
            print(f"An error occurred while navigating to the product page: {e}")


    def add_to_cart(self):
        print(" ")
        print("Adding to the cart..")
        product_name = self.driver.find_element(By.XPATH, "//h1[@class='page-title']/span").text.strip().lower()
        self.driver.execute_script("window.scrollBy(0, 200);")
        add = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @title='Add to Cart']"))
        )
        add.click()
        time.sleep(3)

        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
            )
        )

        # Step 4: Verify that the success message contains the correct product name
        success_message_text = success_message.text.strip().lower()
        assert product_name in success_message_text, f"Expected product name '{product_name}' not found in success message: {success_message_text}"

    def go_to_cart(self):
        print(" ")
        print("Go to cart..")
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'action viewcart') and contains(@href, '/checkout/cart/') and normalize-space() = 'View and edit cart']"))
        )
        cart.click()
        time.sleep(3)

    def go_to_shipping(self):
        print(" ")
        print("Go to shipping..")
        self.driver.execute_script("window.scrollBy(0, 200);")
        shipping = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @data-role='proceed-to-checkout' and @title='Proceed to Checkout' and @class='action primary checkout']"))
        )
        shipping.click()
        time.sleep(3)

    def fill_the_shipping_details(self):
        email = "d.noel251299@gmail.com"
        f_name = "Noel"
        l_name = "DurairajPersonal"
        s_address = "testAddress"
        z_code = "testZipCode"
        city = "City"
        p_number = "1231231232"
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email' and @id='customer-email' and @class='input-text']"))
        )
        email_field.clear()
        email_field.send_keys(email)
        first_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='firstname' and @class='input-text']"))
        )
        first_name.clear()
        first_name.send_keys(f_name)
        last_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='lastname' and @class='input-text']"))
        )
        last_name.clear()
        last_name.send_keys(l_name)

        street_address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='street[0]' and @class='input-text']"))
        )
        street_address.send_keys(s_address)
        post_code = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='postcode' and @class='input-text']"))
        )
        post_code.clear()
        post_code.send_keys(z_code)
        city_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='city' and @class='input-text']"))
        )
        city_field.clear()
        city_field.send_keys(city)
        phone_number = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='telephone' and @class='input-text']"))
        )
        phone_number.clear()
        phone_number.send_keys(p_number)

        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 500);")
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit' and contains(@class, 'button action continue primary')]")
            )
        )
        next_button.click()
        time.sleep(3)

    def fill_the_payement(self):
        print(" ")
        print("Test payments & review")
        cod = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='radio' and contains(@id, 'cashondelivery')]")
            )
        )
        cod.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 200);")
        checkbox = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='checkbox' and contains(@id, 'cashondelivery') and @name='agreement[1]']")
            )
        )
        checkbox.click()
        print("placing the order..")
        self.driver.execute_script("window.scrollBy(0, 200);")
        place_order_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[@type='submit' and contains(@class, 'action primary checkout') and @title='Place Order']")
            )
        )
        place_order_button.click()
        time.sleep(5)

    def is_savedaddress_there(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='shipping-address-item selected-item']")
                )
            )
            return True  # Saved address is present
        except TimeoutException:
            return False  # Saved address is not present

    def add_new_address(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        # Click on "Add New Address" button
        add_address_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-new-address']"))
        )
        add_address_button.click()

        f_name = "Noel1"
        l_name = "DurairajPersonal1"
        s_address = "testAddress1"
        z_code = "testZipCode1"
        city = "City1"
        p_number = "12312312321"
        first_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='firstname' and @class='input-text']"))
        )
        first_name.clear()
        first_name.send_keys(f_name)
        last_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='lastname' and @class='input-text']"))
        )
        last_name.clear()
        last_name.send_keys(l_name)

        street_address = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='street[0]' and @class='input-text']"))
        )
        street_address.send_keys(s_address)
        post_code = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='postcode' and @class='input-text']"))
        )
        post_code.clear()
        post_code.send_keys(z_code)
        city_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='city' and @class='input-text']"))
        )
        city_field.clear()
        city_field.send_keys(city)
        phone_number = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='text' and @name='telephone' and @class='input-text']"))
        )
        phone_number.clear()
        phone_number.send_keys(p_number)

        # Submit the form
        submit_button = self.driver.find_element(By.XPATH, "//button[@id='submit-address']")
        submit_button.click()

        # Wait for the popup to close or the address to be saved
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.XPATH, "//div[@class='popup-class']"))
        )
        print("New address added successfully.")
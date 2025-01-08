import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MarketingRules:
    def __init__(self, driver):
        self.driver = driver

    def redirect_to_home_page(self):
        self.driver.get("https://uatnew.bonz.com/en")


    def redirect_to_product_page(self):
        self.driver.get("https://uatnew.bonz.com/en/testAutomationSimple")

    def check_catelog_price_discout(self):
        expected = "nz$900.00"
        actual = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "price"))
        )

        # Extract the text from the element
        value = actual.text  # Use `.text` to get the visible text of the element

        # Optionally, apply toLowerCase using JavaScript (if necessary)
        result = self.driver.execute_script("return arguments[0].toLowerCase()", value)
        print(result)  # Print the processed value

        # Check the result against the expected value
        if result == str(expected):
            print("The catelog price ruled applied price is updated successfully in the product page.")
        else:
            print(f"The price does not match the catelog price ruled applied price. Expected: {expected}, Found: {result}")

        time.sleep(2)


    def add_to_cart(self):
        print(" ")
        print("Adding to the cart..")
        product_name = self.driver.find_element(By.XPATH, "//h1[@class='page-title']/span").text.strip().lower()
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

    def check_price_without_coupon(self):
        print(" ")
        print("Checking the discounted price without the coupon applied..")





import time
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPriceRuleManagement:
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


    def nav_to_new_cart_price_rule(self):
        create_order = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add" and @title="Add New Rule"]'))
        )
        create_order.click()
        print("Successfully redirected to new cart price rule creation form")


    # Locators
    RULE_NAME = (By.XPATH, "//*[@name='name']")
    ACTIVE = (By.XPATH, "/html/body/div[2]/main/div[2]/div/div/div/div[2]/div[1]/div[2]/fieldset/div[3]/div[2]/div/label")
    WEBSITES = (By.NAME, "website_ids")  # Replace with actual locator
    CUSTOMER_GROUPS = (By.NAME, "customer_group_ids")  # Replace with actual locator
    # COUPON



    def fill_mandatory_fields(self, rule_name, percentage, sku, is_with_coupon, coupon_name=""):
        # 1. Enter the rule name
        self.driver.find_element(*self.RULE_NAME).send_keys(rule_name)
        print("Rule name entered.")

        # 2. Check the toggle active bar to make the rule activate
        try:
            # Locate the toggle bar element
            active = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ACTIVE)
            )

            # Check if the toggle bar is already enabled
            if active.get_attribute("value") == "0":  # Assuming '0' means inactive
                active.click()  # Activate the toggle bar
                print("Toggle activated.")
            else:
                print("Toggle already active.")
        except Exception as e:
            print(f"Error with toggle activation: {e}")

        # 3. Select all options for WEBSITES
        try:
            select_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.WEBSITES)
            )
            select = Select(select_element)

            for option in select.options:
                select.select_by_value(option.get_attribute("value"))
            print("All websites selected.")
        except Exception as e:
            print(f"Error selecting websites: {e}")

        # 4. Select all options for CUSTOMER GROUPS
        try:
            select_element1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CUSTOMER_GROUPS)
            )
            select1 = Select(select_element1)

            for option1 in select1.options:
                select1.select_by_value(option1.get_attribute("value"))
            print("All customer groups selected.")
        except Exception as e:
            print(f"Error selecting customer groups: {e}")

        # ----------- Handling Coupon (with or without)
        if is_with_coupon:
            if coupon_name:
                try:
                    print("Processing coupon selection...")

                    # Wait for coupon type dropdown
                    coupon_dropdown = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        "//select[@name='coupon_type']"))
                    )
                    coupon_dropdown.click()
                    time.sleep(1)

                    # Select 'Specific Coupon' option from the dropdown
                    specific_coupon_option = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//option[@value='2' and text()='Specific Coupon']"))
                    )
                    specific_coupon_option.click()
                    print("Coupon 'Specific Coupon' selected.")

                    # Find the coupon code input field
                    coupon_code_input = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH,
                                                          "//input[@name='coupon_code']"))
                    )
                    coupon_code_input.send_keys(coupon_name)
                    print(f"Coupon name '{coupon_name}' entered.")

                except Exception as e:
                    print(f"Error selecting coupon: {e}")
            else:
                print("Coupon name is missing!")
        else:
            print("No coupon selected.")


        time.sleep(1)

        # SELECTING THE CONDITION
        condition = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(@class, 'admin__collapsible-title') and span[@data-bind=\"i18n: label\" and text()='Conditions']]"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", condition)
        condition.click()

        try:
            # Wait for the '+' icon to be clickable
            add_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//ul[@id='conditions__1__children']//a[@class='label']/img[contains(@class, 'rule-param-add') and @title='Add']"))
            )
            # Click the '+' icon
            add_icon.click()
            print("Successfully clicked the '+' icon.")

            # Wait for the dropdown to be visible
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "//select[@id='conditions__1__new_child']"))
            )
            dropdown.click()
            time.sleep(2)

            # Wait for the options to be visible and select 'Product attribute combination' value
            sku_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//option[text()='Product attribute combination']"))
            )
            sku_option.click()

            print("Successfully selected 'Product attribute combination' from the dropdown.")

            # --------------
            time.sleep(2)
            # Wait for the '+' icon to be clickable
            add_icon1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//span[contains(@class, 'rule-param-new-child')]//a[contains(@class, 'label')]//img[contains(@class, 'rule-param-add') and contains(@class, 'v-middle') and @title='Add']"))
            )
            # Click the '+' icon
            add_icon1.click()
            print("Successfully clicked the second '+' icon.")

            time.sleep(2)

            # Wait for the dropdown to be visible
            dropdown1 = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "//span[contains(@class, 'rule-param-new-child')]//select[contains(@class, 'element-value-changer') and @id='conditions__1--1__new_child']"))
            )
            dropdown1.click()
            time.sleep(2)

            # Wait for the options to be visible and select 'Product attribute combination' value
            sku_option = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//option[text()='SKU']"))
            )
            sku_option.click()

            # Wait for the ellipsis icon to be clickable
            ellipsis = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//span[contains( @class , 'rule-param')] // a[contains( @ class, 'label') and text()='...']"))
            )
            # Click the ellipsis icon
            ellipsis.click()


            # Wait for the text field to be visible
            sku_textfield = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                "//span[contains(@class , 'element')] // input[@ id='conditions__1--1--1__value' and contains( @ class, 'input-text')]"))
            )
            sku_textfield.send_keys(sku)

            apply = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'rule-param-apply')]//img[@alt='Apply']"))
            )
            apply.click()


        except Exception as e:
            print(f"Error occurred: {e}")


        time.sleep(3)

        # Select the actions
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
        print("Successfully types the percentage of the discount")
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
            print("Save bjtt")
        except InvalidSelectorException:
            print("Invalid selection is selected")
import time
from logging import exception
from time import process_time_ns

from pycparser.c_ast import Return
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateCMS:
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
            print("Blocking notifications closed.")
        except TimeoutException:
            print("No blocking notifications appeared.")

# Creating a CMS Page
    def nav_to_add_new(self):
        # Click the arrow or button to open the dropdown
        try:
            add_new = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="add"]'))
            )
            add_new.click()
            return True
        except Exception as e:
            print(f"Error while clicking the add new button: {e}")
            return False

    def check_enable_toggle(self):
        try:
            active = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@class='admin__actions-switch-checkbox' and @name='is_active']"))
            )
            # Check if the toggle bar is already enabled
            if active.get_attribute("value") == "0":  # Assuming '0' means inactive
                active.click()  # Activate the toggle bar
                print("Toggle activated.")
                return True
            else:
                print("Toggle already active.")
                return True
        except TimeoutException as e:
            print(f"Error while locating the enable toggle bar: {e}")
            # self.driver.save_screenshot("Tests/visible-part-of-screen.png")
            return False

    # Method to fill mandatory fields
    def fill_mandatory_fields(self, page_t):
            # Wait for and fill 'Page Title'
            page_title = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@class='admin__control-text' and @name='title' and @maxlength='255']"))
            )
            page_title.clear()
            page_title.send_keys(page_t)

            print("Page title filled successfully.")

    def fill_content(self, conten_h, content_b):
        try:
            # Go to the adding content to the content section
            content = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='fieldset-wrapper-title' and @data-state-collapsible='closed']//strong[contains(@class, 'admin__collapsible-title')]//span[text()='Content']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       content)
            content.click()

            time.sleep(2)
            #fill content heading
            content_heading = self.driver.find_element(By.XPATH, "//input[@class='admin__control-text' and @name='content_heading' and @maxlength='255']")
            content_heading.clear()
            content_heading.send_keys(conten_h)
            time.sleep(2)

            #fill content
            iframe = WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='cms_page_form_content_ifr']"))
            )
            content_body = self.driver.find_element(By.XPATH, "//body[@id='html-body' and @data-id='cms_page_form_content']")

            content_body.clear()
            content_body.send_keys(content_b)
            self.driver.switch_to.default_content()
            time.sleep(2)

            print("Successfully filled the content.")
        except TimeoutException as e:
            print(f"Error while filling the content : {e}")

    # Method to save the product
    def save(self):
        time.sleep(2)
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            save_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="save-button"]/span'))
            )
            # Scroll the element into view before clicking
            # self.driver.execute_script("arguments[0].scrollIntoView();", save_button)

            save_button.click()
            print("CMS Page saved successfully.")
            time.sleep(2)
        except Exception as e:
            print(f"Error while saving the CMS Page: {e}")


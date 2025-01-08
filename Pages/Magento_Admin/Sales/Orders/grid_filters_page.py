import time
from datetime import datetime

# from tkinter import Image
from PIL import Image
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators
import os
screenshot_path = os.path.join("screenshots", "screenshot.png")

class GridFilters:
    def __init__(self, driver):
        # self.wait = None
        # self.driver = driver
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.screenshot_dir = "./screenshots"  # Directory to save screenshots
        os.makedirs(self.screenshot_dir, exist_ok=True)  # Create directory if it doesn't exist

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

    def click_filter_option(self):
        # Find and click the filter button
        filter_button = self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[2]/div[1]/div[3]/div/button')
        filter_button.click()

    def nav_to_new_order(self):
        try:
            screenshot_name = "full_page_screenshot.png"
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)

            # Find and click the filter button
            filter_button = self.driver.find_element(By.XPATH,
                                                     '//*[@id="container"]/div/div[2]/div[1]/div[3]/div/button')
            filter_button.click()
            filter_button.click()
            # Take full-page screenshot
            self.take_full_page_screenshot(screenshot_path)

            # Validate and print confirmation
            if os.path.exists(screenshot_path):
                print(f"Screenshot saved successfully at: {screenshot_path}")
            else:
                print(f"Screenshot failed to save at: {screenshot_path}")

        except Exception as e:
            print(f"Error while clicking the filter option: {e}")

    def filter_by_purchase_date(self, from_date, to_date=None):
        """
        Filters the orders grid by purchase date range.

        Args:
            from_date (str): The start date in 'mm/dd/yyyy' format.
            to_date (str, optional): The end date in 'mm/dd/yyyy' format. Defaults to None.
        """
        try:
            # Locate the 'From Date' input field
            from_date_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='created_at[from]' and contains(@class, '_has-datepicker')]"))
            )
            from_date_input.clear()
            from_date_input.send_keys(from_date)

            # If 'To Date' is provided, locate the 'To Date' input field
            if to_date:
                to_date_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@name='created_at[to]' and contains(@class, '_has-datepicker')]"))
                )
                to_date_input.clear()
                to_date_input.send_keys(to_date)

            self.apply_filters()
            time.sleep(5)
            print(f"Filter applied for purchase date: {from_date} to {to_date or from_date}")
        except Exception as e:
            print(f"Error while applying purchase date filter: {e}")

    def verify_filtered_results(self, start_date, end_date=None):
        """
        Verifies the filtered results based on the purchase date.

        Args:
            start_date (str): The start date in 'mm/dd/yyyy' format.
            end_date (str, optional): The end date in 'mm/dd/yyyy' format. Defaults to None.

        Returns:
            bool: True if all displayed results match the filter criteria, False otherwise.
        """
        try:
            # Locate all visible purchase date cells in the grid
            date_cells = self.driver.find_elements(By.XPATH, "//td[@data-column='purchase_date']")
            input_date_format = "%m/%d/%Y"
            grid_date_format = "%m/%d/%Y"  # Adjust if grid uses a different format

            for cell in date_cells:
                cell_date = cell.text.strip()

                # Convert the dates to datetime objects for comparison
                cell_date_obj = datetime.strptime(cell_date, grid_date_format)
                start_date_obj = datetime.strptime(start_date, input_date_format)

                if end_date:
                    end_date_obj = datetime.strptime(end_date, input_date_format)
                    if not (start_date_obj <= cell_date_obj <= end_date_obj):
                        print(f"Order with date {cell_date} is outside the range {start_date} - {end_date}.")
                        return False
                else:
                    if cell_date_obj != start_date_obj:
                        print(f"Order with date {cell_date} does not match the filter date {start_date}.")
                        return False

            print("All displayed results match the purchase date filter.")
            return True
        except Exception as e:
            print(f"Error while verifying filtered results: {e}")
            return False

    #if you want to take screenshot of the page then you can use this function to take the screenshot.
    def take_full_page_screenshot(self, screenshot_name="full_page_screenshot"):
        try:
            # Your full-page screenshot logic
            screenshot_dir = "./screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            # Sanitize screenshot name by removing invalid characters
            sanitized_name = screenshot_name.replace('"', '').replace(":", "").replace("?", "")

            # Get the total page height and viewport height
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            viewport_height = self.driver.execute_script("return window.innerHeight")

            # Calculate the scroll positions for 3 screenshots
            first_scroll_position = 0
            second_scroll_position = total_height // 3
            third_scroll_position = 2 * (total_height // 3)

            # Take the first screenshot (top of the page)
            self.driver.execute_script(f"window.scrollTo(0, {first_scroll_position});")
            time.sleep(1)  # Give it time to scroll
            self.driver.save_screenshot(os.path.join(screenshot_dir, f"{sanitized_name}_1.png"))

            # Take the second screenshot (middle of the page)
            self.driver.execute_script(f"window.scrollTo(0, {second_scroll_position});")
            time.sleep(1)  # Give it time to scroll
            self.driver.save_screenshot(os.path.join(screenshot_dir, f"{sanitized_name}_2.png"))

            # Take the third screenshot (bottom of the page)
            self.driver.execute_script(f"window.scrollTo(0, {third_scroll_position});")
            time.sleep(1)  # Give it time to scroll
            self.driver.save_screenshot(os.path.join(screenshot_dir, f"{sanitized_name}_3.png"))

            print(f"Screenshots saved successfully at: {screenshot_dir}")

        except Exception as e:
            print(f"Error while capturing screenshots: {e}")

    # def set_filter(self, locator, value):
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(locator)
    #     )
    #     element.clear()
    #     element.send_keys(value)
    #
    # def apply_filters(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Locators.apply_filters_button)
    #     ).click()
    #
    # def clear_filters(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Locators.clear_filters_button)
    #     ).click()
    #
    # def get_grid_results(self):
    #     rows = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_all_elements_located(Locators.grid_rows)
    #     )
    #     return rows

    # def get_grid_row_text(self, row):
    #     return row.text


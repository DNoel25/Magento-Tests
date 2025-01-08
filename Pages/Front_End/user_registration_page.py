import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserRegistration:
    def __init__(self, driver):
        self.driver = driver

    def confirm_the_page(self):
        h1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="maincontent"]/div[1]/h1'))
        )
        print("Successfully redirected to the user registration page")

    def filling_mandatory_fields(self, first_n, last_n, email, pwd, c_pwd):

        first_name = self.driver.find_element(By.ID, "firstname")
        last_name = self.driver.find_element(By.ID, "lastname")
        email_field = self.driver.find_element(By.ID, "email_address")
        password = self.driver.find_element(By.ID, "password")
        c_password = self.driver.find_element(By.ID, "password-confirmation")

        first_name.send_keys(first_n)
        last_name.send_keys(last_n)
        email_field.send_keys(email)
        password.send_keys(pwd)
        c_password.send_keys(c_pwd)

        # Locate the reCAPTCHA iframe and switch to it
        recaptcha_iframe = WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '//*[@class="g-recaptcha"]/div/div/iframe'))
        )
        print("1")
        confirm_recaptcha = self.driver.find_element(By.XPATH, '*[@class="g-recaptcha"]/div/div/iframe')
        print("2")
        result = self.driver.execute_script("return arguments[0]", confirm_recaptcha)
        confirm_recaptcha.click()

        time.sleep(4)
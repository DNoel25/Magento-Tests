# Pages/side_navigation_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators

class SideNavigationPage:
    def __init__(self, driver):
        self.driver = driver
#---------SALES----------
#Sales module
    def open_catelog_menu(self):
        # Wait for and click on the "catelog" main menu item by indexing
        catelog_module = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.CATELOG_MAIN_MODULE)
        )
        catelog_module.click()
        print("Main menu item 'Catelog' clicked")

#Orders sub module
    def open_products(self):
        # Wait for and click on the "products" main menu item by indexing
        products = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.PRODUCTS_MENU)
        )
        products.click()
        print("Submodule 'Products' clicked")

# ---------CATELOG----------
#catelog module
    def open_sales_menu(self):
        # Wait for and click on the "catelog" main menu item by indexing
        catelog_module = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.SALES_MAIN_MENU)
        )
        catelog_module.click()
        print("Main menu item 'Sales' clicked")

#products sub module
    def open_orders(self):
        # Wait for and click on the "products" main menu item by indexing
        products = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.ORDERS_MENU)
        )
        products.click()
        print("Submodule 'Orders' clicked")
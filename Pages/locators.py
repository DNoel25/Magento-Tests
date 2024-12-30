# Pages/locators.py

from selenium.webdriver.common.by import By

class Locators:

#Catelog module
    CATELOG_MAIN_MODULE = (By.XPATH, "//li[@id='menu-magento-catalog-catalog']/a/span[text()='Catalog']")
    #Products module
    PRODUCTS_MENU = (By.XPATH, "//li[@id='menu-magento-catalog-catalog']//li[@data-ui-id='menu-magento-catalog-catalog-products']/a/span[text()='Products']")

#Sales module
    SALES_MAIN_MENU = (By.XPATH, "//li[@id='menu-magento-sales-sales']/a/span[text()='Sales']")
    #Orders module
    ORDERS_MENU = (By.XPATH, "//li[@data-ui-id='menu-magento-sales-sales-order']/a/span[text()='Orders']")

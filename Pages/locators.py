# Pages/locators.py

from selenium.webdriver.common.by import By

class Locators:

#Catelog module
    CATELOG_MAIN_MODULE = (By.XPATH, "//li[@id='menu-magento-catalog-catalog']/a/span[text()='Catalog']")
    #Products module
    PRODUCTS_MENU = (By.XPATH, "//li[@id='menu-magento-catalog-catalog']//li[@data-ui-id='menu-magento-catalog-catalog-products']/a/span[text()='Products']")
    CATEGORY_MENU  =((By.XPATH, "//li[@id='menu-magento-catalog-catalog']//li[@data-ui-id='menu-magento-catalog-catalog-categories']/a/span[text()='Categories']"))
#Sales module
    SALES_MAIN_MENU = (By.XPATH, "//li[@id='menu-magento-sales-sales']/a/span[text()='Sales']")
    #Orders module
    ORDERS_MENU = (By.XPATH, "//li[@data-ui-id='menu-magento-sales-sales-order']/a/span[text()='Orders']")


#Customer module
    CUSTOMERS_MAIN_MENU = (By.XPATH, "//li[@id='menu-magento-customer-customer']/a/span[text()='Customers']")
    #all customers module
    ALL_CUSTOMERS_MENU = (By.XPATH, "//li[@data-ui-id='menu-magento-customer-customer-manage']/a/span[text()='All Customers']")

#Marketing module
    MARKETING_MAIN_MENU = (By.XPATH, "//li[@id='menu-magento-backend-marketing']/a/span[text()='Marketing']")
    #catelog price rule module
    CATELOG_PRICE_RULE_MENU = (By.XPATH, "//li[@data-ui-id='menu-magento-catalogrule-promo-catalog']/a/span[text()='Catalog Price Rule']")

    #catelog price rule module
    CART_PRICE_RULE_MENU = (By.XPATH, "//li[@data-ui-id='menu-magento-salesrule-promo-quote']/a/span[text()='Cart Price Rules']")

#Content module
    CONTENT_MAIN_MENU = (By.XPATH, "//li[@id='menu-magento-backend-content']/a/span[text()='Content']")
    #all customers module
    CMS_PAGES_MENU = (By.XPATH, "//li[@data-ui-id='menu-magento-cms-cms-page']/a/span[text()='Pages']")
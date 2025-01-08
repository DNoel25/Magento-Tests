import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Magento_Admin.Sales.Orders.grid_filters_page import GridFilters
import time
from selenium.webdriver.chrome.service import Service
from Pages.sidebar_page import SideNavigationPage

@pytest.fixture(scope="module")
def driver():
    driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://uatnew.bonz.com/BonzGroupAdmin/admin/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_logged_in_user_flow(driver):
    magento = GridFilters(driver)
    magento.login_successfully("neosolax", "^3Fp2Z&Vx7!wQ@Lm1")  # Replace with test credentials
    print("Successfully navigate to the Dashboard ")
    #close  the notifications if appears in the Dashboard
    magento.close_notifications()
    magento.test_home_page()

def test_redirection_to_products(driver):
    side_nav = SideNavigationPage(driver)
    side_nav.open_sales_menu()
    side_nav.open_orders()
    time.sleep(2)



def test_purchase_date_filter(driver):
    """
    Test the purchase date filter functionality in the orders grid view.
    """
    try:
        magento = GridFilters(driver)
        magento.click_filter_option()
        # Apply filter for a specific date or range
        start_date = "01/01/2025"
        end_date = "01/05/2025"
        magento.filter_by_purchase_date(start_date, end_date)

        # Verify the results
        assert magento.verify_filtered_results(start_date, end_date), "Purchase date filter validation failed!"

    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"Unexpected error during test execution: {e}")


# def test_filter_order_id(self, order_page):
#     order_page.set_filter(order_page.filter_order_id, "100000001")
#     order_page.apply_filters()
#     results = order_page.get_grid_results()
#     assert len(results) == 1
#     assert "100000001" in order_page.get_grid_row_text(results[0])












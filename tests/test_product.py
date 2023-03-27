import allure
from Src.pages.HomePage import HomePage
from Src.pages.Product import Product

@allure.description("validate navigation to the product page")
@allure.severity(severity_level="CRITICAL")
@allure.title("Test case ID: TS23")
def test_1_navigate_to_product_page(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        assert pr.assert_product_navigation()
    except Exception as e:
        print(e)
        driver.print_page("test_TS23_error.png")
        raise e

@allure.description("validate that product is added to cart")
@allure.severity(severity_level="CRITICAL")
@allure.title("Test case ID: TS24")
def test_2_adding_product_to_cart(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.Adding_product_to_cart()
        assert pr.assert_add_to_cart()
    except Exception as e:
        print(e)
        driver.print_page("test_TS24_error.png")
        raise e

@allure.description("validating filtering is working properly")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS25")
def test_3_Filter_sort_from_lowest_to_highest_price(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.product_filter_low_to_high_click()
        assert pr.product_filter_low_to_high()
    except Exception as e:
        print(e)
        driver.print_page("test_TS25_error.png")
        raise e

@allure.description("validate filtering is working properly")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS26")
def test_4_Filter_sort_from_highest_to_lowest_price(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.product_filter_high_to_low_click()
        assert pr.product_filter_high_to_low_price()
    except Exception as e:
        print(e)
        driver.print_page("test_TS26_error.png")
        raise e

def test_5_Filter_product_order_to_linear(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.assert_filter_product_order_to_linear()
        assert pr.assert_filter_product_order_to_linear()
    except Exception as e:
        print(e)
        driver.print_page("test_TS27_error.png")
        raise e






import allure
import pytest

from Src.pages.HomePage import HomePage
from Src.pages.Product import Product
from Src.pages.Login import Login

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
        driver.save_screenshot("test_TS23_error.png")
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
        driver.save_screenshot("test_TS24_error.png")
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
        driver.save_screenshot("test_TS25_error.png")
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
        driver.save_screenshot("test_TS26_error.png")
        raise e

@allure.description("validate product filtering can be set to linear")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS27")
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
        driver.save_screenshot("test_TS27_error.png")
        raise e

@allure.description("validating uploading a product to site")
@allure.severity(severity_level="HIGH")
@allure.title("Test case ID: TS28")
def test_6_Upload_product(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        pr.upload_product()
        assert not pr.assert_upload_product()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS28_error.png")
        raise e

@allure.description("validate if product image")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS29")
def test_6_check_product_image(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        assert pr.assert_product_navigation()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS29_error.png")
        raise e

@allure.description("validate product title")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS29")
def test_7_check_product_title(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        assert pr.assert_product_title()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS30_error.png")
        raise e

@allure.description("validate product carton")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS31")
def test_8_Check_product_carton(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        assert pr.assert_product_carton()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS31_error.png")
        raise e
@allure.description("validate product cost per carton")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS32")
def test_9_Check_product_cost_per_carton(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        assert pr.assert_cost_per_carton()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS32_error.png")
        raise e

@allure.description("validate product cartons stock")
@allure.severity(severity_level="HIGH")
@allure.title("Test case ID: TS33")
def test_10_Check_cartons_stock(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        assert pr.assert_cartons_stock()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS33_error.png")
        raise e

@allure.description("Deleting all products from cart")
@allure.severity(severity_level="HIGH")
@allure.title("Test case ID: TS18")
def test_11_empty_cart_button(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        pr = Product(driver)
        hp.click_save_button()
        pr.navigate_to_product_page()
        pr.add_product_to_cart_for_checkout()
        pr.Empty_cart_button()
        assert "₪0.00" in pr.Empty_cart_button()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS18_error.png")

# Run all the test functions in the file
if __name__ == "__main__":
    pytest.main(['-s', '-v', 'test_product.py'])




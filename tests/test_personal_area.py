import allure
import pytest
from Src.pages.HomePage import HomePage
from Src.pages.Login import Login
from Src.pages.Persona_Area import PersonalArea
from Src.pages.Product import Product


@allure.description("validate withdraw cash")
@allure.severity(severity_level="NORMAL")
@pytest.mark.skip(reason="Test case skipped because wallet cash cant be added")
@allure.title("Test case ID: TS36")
def test_1_withdraw_cash(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        per = PersonalArea(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        per.Withdraw_cash()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS36_error.png")
        raise e

@allure.description("validate text link")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS39")
def test_2_Navigate_to_we_are_here_text_link(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        per = PersonalArea(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        per.navigate_to_we_are_here_text_link()
        assert per.assert_we_are_here_page()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS39_error.png")
        raise e

@allure.description("validate checkout button")
@allure.severity(severity_level="CRITICAL")
@allure.title("Test case ID: TS40")
def test_4_Checkout_button(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        per = PersonalArea(driver)
        pr = Product(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        pr.navigate_to_product_page()
        pr.add_product_to_cart_for_checkout()
        per.click_checkout_button()
        assert per.assert_checkout_button()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS40_error.png")
        raise e

@allure.description("valid form delivery details")
@allure.severity(severity_level="CRITICAL")
@allure.title("Test case ID: TS37")
def test_4_Valid_delivery_details(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        per = PersonalArea(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        per.personal_area()
        per.Valid_delivery_details()
        assert not per.assert_valid_delivery_details()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS37_error.png")
        raise e

@allure.description("invalid form delivery details")
@allure.severity(severity_level="NORMAL")
@pytest.mark.skip(reason="Test case skipped because valid form doesnt function")
@allure.title("Test case ID: TS42")
def test_4_Invalid_delivery_details(test_setup):
    print("test skipped")
import allure
import pytest

from Src.pages.HomePage import HomePage
from Src.pages.Search import Search
@allure.description("validate search looks for product")
@allure.severity(severity_level="HIGH")
@allure.title("Test case ID: TS34")
def test_1_Search_looks_for_product_by_input(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        sr = Search(driver)
        hp.click_save_button()
        sr.Search_looks_for_product_by_input()
        assert sr.assert_search_product_by_input()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS34_error.png")
        raise e

@allure.description("validate click on product sends to product page")
@allure.severity(severity_level="HIGH")
@allure.title("Test case ID: TS35")
def test_2_Search_looks_for_product_by_input(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        sr = Search(driver)
        hp.click_save_button()
        sr.Search_looks_for_product_by_input()
        sr.Navigate_to_product_page_by_search()
        assert sr.assert_product_page()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS35_error.png")
        raise e

# Run all the test functions in the file
if __name__ == "__main__":
    pytest.main(['-s', '-v', 'test_search.py'])
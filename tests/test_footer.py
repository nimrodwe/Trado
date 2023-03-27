import time

from Src.pages.HomePage import HomePage
from Src.pages.Footer import Footer

def test_1_navigate_to_facebook(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.navigate_to_facebook()
        assert driver.current_url == 'https://www.facebook.com/'
    except Exception as e:
        print(e)
        driver.print_page("test footer")
        raise e
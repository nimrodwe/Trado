import allure
import pytest

from Src.pages.HomePage import HomePage
from Src.pages.Footer import Footer
from Src.pages.Login import Login


# under "stay in touch" section
@allure.description("navigate to facebook")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS43")
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
        driver.print_page("test_TS43_error.png")
        raise e

# under "stay in touch" section
@allure.description("navigate to instagram")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS44")
def test_2_navigate_to_instagram(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.navigate_to_instagram()
        assert driver.current_url == 'https://www.instagram.com/'
    except Exception as e:
        print(e)
        driver.print_page("test_TS44_error.png")
        raise e

# under "stay in touch" section
@allure.description("navigate to twitter")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS45")
def test_3_navigate_to_twitter(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.navigate_to_twitter()
        assert driver.current_url == 'https://twitter.com/?lang=he'
    except Exception as e:
        print(e)
        driver.print_page("test_TS45_error.png")
        raise e

# under "Additional" section
@allure.description("navigate to common questions")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS46")
def test_4_common_questions(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.navigate_to_common_questions()
        assert driver.current_url == 'https://qa.trado.co.il/questions'
    except Exception as e:
        print(e)
        driver.print_page("test_TS46_error.png")
        raise e

# under "Additional" section
@allure.description("navigate to how delivery works")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS47")
def test_5_how_delivery_works(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.how_delivery_works()
        assert driver.current_url == 'https://qa.trado.co.il/shipment'
    except Exception as e:
        print(e)
        driver.print_page("test_TS47_error.png")
        raise e

# under "Additional" section
@allure.description("navigate to payment solution")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS48")
def test_6_payment_solution(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.payment_solutions()
        assert driver.current_url == 'https://www.max.co.il/cards/card/8649'
    except Exception as e:
        print(e)
        driver.print_page("test_TS48_error.png")
        raise e

# under "Additional" section
@allure.description("navigate to MAX business")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS49")
def test_7_MAX_business(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.MAX_business()
        assert driver.current_url == 'https://www.max.co.il/cards/card/8649'
    except Exception as e:
        print(e)
        driver.print_page("test_TS49_error.png")
        raise e

# under "Importants" section
@allure.description("navigate to who we are")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS50")
def test_8_who_we_are(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        fo = Footer(driver)
        hp.click_save_button()
        fo.who_we_are_link()
        assert driver.current_url == 'https://www.trado.co.il/page'
    except Exception as e:
        print(e)
        driver.print_page("test_TS50_error.png")
        raise e

# under "Importants" section
@allure.description("navigate to personal area")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS51")
def test_9_personal_area(test_setup):
    try:
        driver = test_setup
        fo = Footer(driver)
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        fo.persona_area()
        assert driver.current_url == 'https://qa.trado.co.il/user/personalArea'
    except Exception as e:
        print(e)
        driver.print_page("test_TS51_error.png")
        raise e

# under "Importants" section
@allure.description("navigate to eTrado")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS52")
def test_10_eTrado(test_setup):
    try:
        driver = test_setup
        fo = Footer(driver)
        hp = HomePage(driver)
        hp.click_save_button()
        fo.eTrado()
        assert driver.current_url == 'https://qa.trado.co.il/etrado'
    except Exception as e:
        print(e)
        driver.print_page("test_TS52_error.png")
        raise e

# under "Importants" section
@allure.description("navigate to contact us")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS53")
def test_11_contact_us(test_setup):
    try:
        driver = test_setup
        fo = Footer(driver)
        hp = HomePage(driver)
        hp.click_save_button()
        fo.contact_us()
        assert driver.current_url == 'https://qa.trado.co.il/contact'
    except Exception as e:
        print(e)
        driver.print_page("test_TS53_error.png")
        raise e

# under "Importants" section
@allure.description("navigate to business interface")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS54")
def test_12_business_interface(test_setup):
    try:
        driver = test_setup
        fo = Footer(driver)
        hp = HomePage(driver)
        hp.click_save_button()
        fo.business_interface()
        assert driver.current_url == 'https://qa.trado.co.il/joinUs'
    except Exception as e:
        print(e)
        driver.print_page("test_TS54_error.png")
        raise e

# Run all the test functions in the file
if __name__ == "__main__":
    pytest.main(['-s', '-v', 'test_footer.py'])










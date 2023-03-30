import allure
from Src.pages.HomePage import HomePage
from Src.pages.Login import Login

@allure.description("validate functionality of left arrow")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS02")
def test_1_left_arrow(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        hp.click_left_arrow()
        assert hp.assert_left_arrow().is_displayed()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS02_error.png")
        raise e

@allure.description("validate functionality of right arrow")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS03")
def test_2_right_arrow(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        hp.click_right_arrow()
        assert hp.assert_right_arrow().is_displayed()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS03_error.png")


# negative test (should return failed)
@allure.description("validate functionality of left arrow")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS04")
def test_3_send_details_to_commercial_man_with_tablet(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        hp.send_details_to_commercial_man_with_tablet()
        assert hp.assert_commercial_man_with_tablet()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS04_error.png")
        raise e
@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS05")
def test_4_Navigate_to_Commercial_hand_with_phone_button(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        hp.click_right_arrow()
        hp.commercial_man_with_phone()
        assert hp.assert_commercial_man_with_phone()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS05_error.png")
        raise e

@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS06")
def test_5_Navigate_to_Commercial_man_thumbs_up_button(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        hp.click_right_arrow()
        hp.click_right_arrow()
        hp.commercial_man_thumbs_up()
        assert hp.assert_comercial_man_thumbs_up()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS06_homepage_error.png")
        raise e

@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS07")
def test_6_Navigate_to_Commercial_man_with_packages(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        hp.commercial_man_with_packages()
        assert hp.assert_commercial_man_with_packages()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS07_error.png")
        raise e

@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS08")
def test_7_Navigate_to_Commerical_max_woman(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        hp.commercial_max_woman()
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS08_error.png")
        raise e

@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS09")
def test_8_Navigate_to_Commercial_girl_with_laptop(test_setup):
        try:
            driver = test_setup
            hp = HomePage(driver)
            lgn = Login(driver)
            hp.click_save_button()
            lgn.move_to_login()
            lgn.login("0586691039")
            lgn.submit_login()
            lgn.login_input_squares()
            lgn.submit_secret_code()
            hp.commercial_girl_with_laptop()
        except Exception as e:
            print(e)
            driver.save_screenshot("test_TS09_error.png")
            raise e

@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS10")
def test_9_Navigate_to_Commercial_open_box(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        hp.commercial_open_box()
        assert hp.assert_commercial_open_box()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS10_error.png")
        raise e

@allure.description("validate navigation to the commercal")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS11")
def test_10_Navigate_to_woman_with_smoothie(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("0586691039")
        lgn.submit_login()
        lgn.login_input_squares()
        lgn.submit_secret_code()
        hp.commercial_woman_with_smoothie()
        assert driver.current_url == "https://www.max.co.il/cards/card/8649"
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS11_error.png")
        raise e

@allure.description("Check text element in paragraph")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS12")
def test_11_Common_question_description_text(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        assert hp.assert_Common_question_description_text()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS12_error.png")
        raise e

@allure.description("navigate to all questions in homepage")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS13")
def test_12_navigate_to_all_questions(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        hp.navigate_to_all_questions()
        assert hp.assert_to_all_questions()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS13_error.png")
        raise e

@allure.description("Check contact us element xpath")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS14")
def test_13_Contact_description_text(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        assert hp.assert_Contact_description_text()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS14_error.png")
        raise e

@allure.description("navigate to contact us")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS15")
def test_14_Navigate_to_contact_us(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        hp.Navigate_to_contact_us()
        assert hp.assert_contact_us_page()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS15_error.png")
        raise e

@allure.description("How shipment works description text")
@allure.severity(severity_level="LOW")
@allure.title("Test case ID: TS16")
def test_15_How_shipment_works_description_text(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        assert hp.assert_How_shipment_works_description_text()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS16_error.png")
        raise e

@allure.description("How shipment works description text")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS17")
def test_16_Navigate_to_more_details(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        hp.click_save_button()
        hp.Navigate_to_more_details()
        assert hp.assert_Navigate_to_more_details()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS17_error.png")
        raise e






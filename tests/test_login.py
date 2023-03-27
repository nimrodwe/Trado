import allure

from Src.pages.HomePage import HomePage
from Src.pages.Login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# login to user
@allure.description("sanity check if a user can login")
@allure.severity(severity_level="CRITICAL")
@allure.title("Test case ID: TS19")
def test_1_valid_login(test_setup):
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
        text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > '
                                                                                                 'div.pages_pages > '
                                                                                                 'header > div > div > '
                                                                                                 'a.header_userAreaLink')))\
            .get_attribute("innerText")
        assert text != 'שלום אורח,\nהתחברות"'
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS19_error.png")
        raise e

# negative login test
@allure.description("to check if a user can register with invalid credantials")
@allure.severity(severity_level="NORMAL")
@allure.title("Test case ID: TS20")
def test_2_invalid_login(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        hp.click_save_button()
        lgn.move_to_login()
        lgn.login("5557777788")
        lgn.submit_login()
        form_message_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[3]'
        form_message = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, form_message_xpath))).get_attribute("innertext")
        assert form_message == "No Such User Please Register"
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS20_error.png")


import allure
from Src.pages.HomePage import HomePage
from Src.pages.Login import Login
from Src.pages.Register import Register

@allure.description("valid register to website")
@allure.severity(severity_level="HIGH")
@allure.title("Test case ID: TS21")
def test_1_valid_register(test_setup):
    try:
        driver = test_setup
        hp = HomePage(driver)
        lgn = Login(driver)
        reg = Register(driver)
        hp.click_save_button()
        lgn.move_to_login()
        reg.move_to_register()
        reg.register()
        assert reg.assert_register()
    except Exception as e:
        print(e)
        driver.save_screenshot("test_TS21_error.png")
        raise e

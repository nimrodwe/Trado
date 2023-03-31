from selenium.webdriver.common.by import By
from common import CommonOps
from Src.Utils.getUserKeyCode import find_db_login_key_register
from Src.Utils.getUserKeyCode import generate_phone_number

class Register(CommonOps):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_register(self):
        register_menu_button_xpath = '/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/span[2]'
        return self.wait_for((By.XPATH, register_menu_button_xpath)).click()

    def register(self):
        phone_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
        id = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'
        read_checkbox_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/span/span/i'
        login_button_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/input'
        first_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
        random_phone_number = generate_phone_number()
        self.wait_for((By.XPATH, phone_input_xpath)).send_keys(random_phone_number)
        self.wait_for((By.XPATH, id)).send_keys("4")
        self.wait_for((By.XPATH, read_checkbox_xpath)).click()
        self.wait_for((By.XPATH, login_button_xpath)).click()
        phone_code = find_db_login_key_register(random_phone_number)
        self.wait_for((By.XPATH, first_input_xpath)).send_keys(phone_code)

    def assert_register(self):
        create_button_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/div/div[3]/button'
        return self.wait_for((By.XPATH, create_button_xpath))

    def Invalid_register(self):
        phone_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
        id = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'
        read_checkbox_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/span/span/i'
        login_button_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/input'
        first_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
        random_phone_number = generate_phone_number()
        self.wait_for((By.XPATH, phone_input_xpath)).send_keys("0586691039")
        self.wait_for((By.XPATH, id)).send_keys("4")
        self.wait_for((By.XPATH, read_checkbox_xpath)).click()
        self.wait_for((By.XPATH, login_button_xpath)).click()
        phone_code = find_db_login_key_register(random_phone_number)
        self.wait_for((By.XPATH, first_input_xpath)).send_keys(phone_code)

    def assert_invalid_register(self):
        error_message = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[3]'
        self.wait_for((By.XPATH, error_message))





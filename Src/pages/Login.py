from selenium.webdriver.common.by import By
from selenium import webdriver
from common import CommonOps
from Src.Utils.getUserKeyCode import find_db_login_key
class Login(CommonOps):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_login(self):
        move_button_selector = '//*[@id="root"]/div/div[2]/header/div/div/a[1]'
        return self.wait_for((By.XPATH, move_button_selector)).click()

    def login(self, number):
        phone_input = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
        return self.wait_for((By.XPATH, phone_input)).send_keys(number)

    def submit_login(self):
        submit_button = '//*[@id="root"]/div/div[4]/div/div/div/div/form/input'
        return self.wait_for((By.XPATH, submit_button)).click()

    def submit_secret_code(self):
        submit_button = '//*[@id="root"]/div/div[4]/div/div/div/div/form/input'
        return self.wait_for((By.XPATH, submit_button)).click()

    def login_input_squares(self):
        first_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input'
        second_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input'
        third_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/input'
        fourth_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[4]/span/input'
        fifth_input_xpath = '//*[@id="root"]/div/div[4]/div/div/div/div/form/div[1]/div[5]/span/input'

        code_list = find_db_login_key()
        user_code_list = []

        for letter in code_list:
            user_code_list.append(letter)

        self.wait_for((By.XPATH, first_input_xpath)).send_keys(user_code_list[0])
        self.wait_for((By.XPATH, second_input_xpath)).send_keys(user_code_list[1])
        self.wait_for((By.XPATH, third_input_xpath)).send_keys(user_code_list[2])
        self.wait_for((By.XPATH, fourth_input_xpath)).send_keys(user_code_list[3])
        self.wait_for((By.XPATH, fifth_input_xpath)).send_keys(user_code_list[4])




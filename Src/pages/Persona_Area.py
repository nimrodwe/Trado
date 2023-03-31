from selenium.webdriver.common.by import By
from common import CommonOps

class PersonalArea(CommonOps):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def personal_area(self):
        personal_area_xpath = '//*[@id="root"]/div/div[2]/header/div/div/a[1]'
        self.wait_for((By.XPATH, personal_area_xpath)).click()

    def Withdraw_cash(self):
        personal_area_xpath = '//*[@id="root"]/div/div[2]/header/div/div/a[1]'
        withdraw_button = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/section/button'
        self.wait_for((By.XPATH, personal_area_xpath)).click()
        self.wait_for((By.XPATH, withdraw_button)).click()

    def navigate_to_we_are_here_text_link(self):
        personal_area_xpath = '//*[@id="root"]/div/div[2]/header/div/div/a[1]'
        we_are_here_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/span/a'
        self.wait_for((By.XPATH, personal_area_xpath)).click()
        self.wait_for((By.XPATH, we_are_here_button_xpath)).click()

    def assert_we_are_here_page(self):
        page_message_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/h4'
        return self.wait_for((By.XPATH, page_message_xpath))

    def click_checkout_button(self):
        checkout_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[3]/button'
        self.wait_for((By.XPATH, checkout_button_xpath)).click()

    def assert_checkout_button(self):
        next_page_message_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/h1'
        return self.wait_for((By.XPATH, next_page_message_xpath))

    def Valid_delivery_details(self):
        edit_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[4]'
        save_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/input'
        first_name_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[1]/span/input'
        last_name_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[2]/span/input'
        phone_number_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[3]/span/input'
        email_address_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[4]/span/input'
        user_id_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[1]/div[5]/span/input'
        city_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[1]/input'
        number_address_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/form/div[2]/div/div[1]/div[2]/span/input'
        new_card_button_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div[2]/div/div'

        # credit card form
        credit_card_number_xpath = '//*[@id="credit-card-input"]'
        id_number_xpath = '//*[@id="userId-input"]'
        month_button_expertion_date_xpath = '//*[@id="expmonth"]'
        fifth_month_expiration_date_xpath = '//*[@id="expmonth"]/option[6]'
        year_button_expiration_date_xpath = '//*[@id="expyear"]'
        year_2024_button_expiration_date_xpath = '//*[@id="expyear"]/option[3]'
        cvv_xpath = '//*[@id="cvv"]'
        add_pay_button_xpath = '//*[@id="btnSubmit"]'

        # filling all inputs
        self.wait_for((By.XPATH, edit_button_xpath)).click()
        self.wait_for((By.XPATH, first_name_xpath)).send_keys("john")
        self.wait_for((By.XPATH, last_name_xpath)).send_keys("amir")
        self.wait_for((By.XPATH, phone_number_xpath)).clear()
        self.wait_for((By.XPATH, phone_number_xpath)).send_keys("0586691039")
        self.wait_for((By.XPATH, email_address_xpath)).send_keys("john123@gmail.com")
        self.wait_for((By.XPATH, user_id_xpath)).send_keys("3")
        self.wait_for((By.XPATH, city_xpath)).send_keys("netanya")
        self.wait_for((By.XPATH, number_address_xpath)).send_keys("5")

        # filing out credit card form
        self.wait_for((By.XPATH, new_card_button_xpath)).click()
        self.driver.switch_to.frame('yaadFrame')
        self.wait_for((By.XPATH, credit_card_number_xpath)).send_keys("4580000000000000")
        self.wait_for((By.XPATH, id_number_xpath)).send_keys("207887704")
        self.wait_for((By.XPATH, month_button_expertion_date_xpath)).click()
        self.wait_for((By.XPATH, fifth_month_expiration_date_xpath)).click()
        self.wait_for((By.XPATH, year_button_expiration_date_xpath)).click()
        self.wait_for((By.XPATH, year_2024_button_expiration_date_xpath)).click()
        self.wait_for((By.XPATH, cvv_xpath)).send_keys("123")
        self.wait_for((By.XPATH, add_pay_button_xpath)).click()

        # add payment
        self.wait_for((By.XPATH, save_button_xpath)).click()

    def assert_valid_delivery_details(self):
        error_message_xpath = '//*[@id="CC_Form"]/div[2]'
        return self.wait_for((By.XPATH, error_message_xpath))





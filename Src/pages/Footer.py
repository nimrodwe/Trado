from common import CommonOps
from selenium.webdriver.common.by import By



class Footer(CommonOps):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_facebook(self):
        facebook_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/a[1]'
        element = self.wait_for((By.XPATH, facebook_button_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def navigate_to_instagram(self):
        instagram_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/a[2]'
        element = self.wait_for((By.XPATH, instagram_button_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def navigate_to_twitter(self):
        twitter_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/a[3]'
        element = self.wait_for((By.XPATH, twitter_button_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def navigate_to_common_questions(self):
        common_questions_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[1]'
        self.wait_for((By.XPATH, common_questions_button_xpath)).click()

    def how_delivery_works(self):
        how_delivery_works = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[2]'
        self.wait_for((By.XPATH, how_delivery_works)).click()

    def payment_solutions(self):
        payment_solutions_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[3]'
        element = self.wait_for((By.XPATH, payment_solutions_button_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def MAX_business(self):
        MAX_business_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[2]/a[4]'
        element = self.wait_for((By.XPATH, MAX_business_button_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def who_we_are_link(self):
        who_we_are_link_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[1]'
        element = self.wait_for((By.XPATH, who_we_are_link_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def persona_area(self):
        persona_area_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[2]'
        self.wait_for((By.XPATH, persona_area_button_xpath)).click()

    def eTrado(self):
        eTrado_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[3]'
        self.wait_for((By.XPATH, eTrado_button_xpath)).click()

    def contact_us(self):
        contact_us_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[4]'
        self.wait_for((By.XPATH, contact_us_button_xpath)).click()

    def business_interface(self):
        business_interface_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/a[5]'
        self.wait_for((By.XPATH, business_interface_button_xpath)).click()


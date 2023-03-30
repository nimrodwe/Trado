from common import CommonOps
from selenium.webdriver.common.by import By

class Search(CommonOps):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Search_looks_for_product_by_input(self):
        search_input_xpath = '//*[@id="root"]/div/div[2]/header/div/div/div/span/input'
        self.wait_for((By.XPATH, search_input_xpath)).send_keys("למון קוש")

    def assert_search_product_by_input(self):
        product_card_xpath = '//*[@id="root"]/div/div[2]/header/div/div/div/div[1]/div/a[1]/div'
        self.wait_for((By.XPATH, product_card_xpath))

    def Navigate_to_product_page_by_search(self):
        search_input_xpath = '//*[@id="root"]/div/div[2]/header/div/div/div/span/input'
        product_card_xpath = '//*[@id="root"]/div/div[2]/header/div/div/div/div[1]/div/a[1]/div'
        self.wait_for((By.XPATH, search_input_xpath)).send_keys("למון קוש")
        self.wait_for((By.XPATH, product_card_xpath)).click()

    def assert_product_page(self):
        product_image_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/img'
        return self.wait_for((By.XPATH, product_image_xpath))


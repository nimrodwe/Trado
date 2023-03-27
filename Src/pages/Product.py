from common import CommonOps
from selenium.webdriver.common.by import By


class Product(CommonOps):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Adding_product_to_cart(self):
        product_card_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[3]/div/div[2]'
        self.wait_for((By.XPATH, product_card_xpath)).click()
        product_add_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/span[1]/i'
        self.wait_for((By.XPATH, product_add_xpath)).click()

    def assert_add_to_cart(self):
        card_in_cart_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/a/div'
        return self.wait_for((By.XPATH, card_in_cart_xpath))

    def navigate_to_product_page(self):
        product_card_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[3]/div/div[2]'
        self.wait_for((By.XPATH, product_card_xpath)).click()

    def assert_product_navigation(self):
        product_img = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/img'
        return self.wait_for((By.XPATH, product_img))

    def product_filter_low_to_high_click(self):
        # change the overall product filter from lowest price to the highest
        drop_down_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select'
        lowest_price_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select/option[2]'
        self.wait_for((By.XPATH, drop_down_xpath)).click()
        self.wait_for((By.XPATH, lowest_price_xpath)).click()

    def product_filter_low_to_high_price(self):
        # taking a middle product price in the middle of a product list line and transfering it into a number
        middle_item_in_list_price = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[2]/div/div[2]/div[2]/div[2]/div/div/span/span')).get_attribute("innertext")
        middle_item_in_list_price_replaced = middle_item_in_list_price.replace("₪", "")
        if middle_item_in_list_price_replaced.isdigit():
            first_item_price_replaced = int(middle_item_in_list_price_replaced)

        # taking a right product price in the middle of a product list line and transfering it into a number
        right_item_price = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div/div/span/span')).get_attribute('innertext')
        right_item_price_replaced = right_item_price.replace("₪", "")
        if right_item_price_replaced.isdigit():
            right_item_price_replaced = int(right_item_price_replaced)

        # taking a left product price in the middle of a product list line and transfering it into a number
        left_item_price = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[3]/div/div[2]/div[2]/div[2]/div/div/span/span')).get_attribute('innertext')
        left_item_price_replaced = left_item_price.replace("₪", "")
        if left_item_price_replaced.isdigit():
            left_item_price_replaced = int(left_item_price_replaced)

        # validating for the assertion in the test to check if the list is filtered in the right order
        assertion = False
        if right_item_price_replaced < middle_item_in_list_price_replaced < left_item_price_replaced:
            assertion = True
        return assertion

    def product_filter_high_to_low_click(self):
        # change the overall product filter from highest price to the lowest
        drop_down_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select'
        highest_price_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/select/option[3]'
        self.wait_for((By.XPATH, drop_down_xpath)).click()
        self.wait_for((By.XPATH, highest_price_xpath)).click()

    def product_filter_high_to_low_price(self):
        # taking a middle product price in the middle of a product list line and transfering it into a number
        middle_item_in_list_price = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[2]/div/div[2]/div[2]/div[2]/div/div/span/span')).get_attribute("innertext")
        middle_item_in_list_price_replaced = middle_item_in_list_price.replace("₪", "")
        if middle_item_in_list_price_replaced.isdigit():
            first_item_price_replaced = int(middle_item_in_list_price_replaced)

        # taking a right product price in the middle of a product list line and transfering it into a number
        right_item_price = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[3]/div/div[2]/div[2]/div[2]/div/div/span/span')).get_attribute('innertext')
        right_item_price_replaced = right_item_price.replace("₪", "")
        if right_item_price_replaced.isdigit():
            right_item_price_replaced = int(right_item_price_replaced)

        # taking a left product price in the middle of a product list line and transfering it into a number
        left_item_price = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div/div/span/span')).get_attribute('innertext')
        left_item_price_replaced = left_item_price.replace("₪", "")
        if left_item_price_replaced.isdigit():
            left_item_price_replaced = int(left_item_price_replaced)

        # validating for the assertion in the test to check if the list is filtered in the right order
        assertion = False
        if right_item_price_replaced < middle_item_in_list_price_replaced < left_item_price_replaced:
            assertion = True
        return assertion

    def Filter_product_order_to_linear(self):
        linear_order_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[4]/span[1]'
        self.wait_for((By.XPATH, linear_order_xpath)).click()

    def assert_filter_product_order_to_linear(self):
        product_card_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[1]/div'
        return self.wait_for((By.XPATH, product_card_xpath))



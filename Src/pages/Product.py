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

    def upload_product(self):
        upload_new_product_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/a[5]/span'
        self.wait_for((By.XPATH, upload_new_product_xpath)).click()

        cop_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[1]/div[1]/div[1]/span/input'
        buissness_name_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[1]/div[1]/div[2]/span/input'
        phone_number_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[2]/div[1]/div[1]/span/input'
        mail_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[2]/div[1]/div[2]/span/input'
        buissness_url_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[3]/div[1]/div[1]/span/input'
        town_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[3]/div[1]/div[2]/span/input'
        street_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[4]/div[1]/div[1]/span/input'
        building_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[2]/div[4]/div[1]/div[2]/span/input'
        add_button = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/input'

        self.wait_for((By.XPATH, cop_xpath)).send_keys('3')
        self.wait_for((By.XPATH, buissness_name_xpath)).send_keys('IQA')
        self.wait_for((By.XPATH, phone_number_xpath)).send_keys('0556961922')
        self.wait_for((By.XPATH, mail_xpath)).send_keys('moshe@IQA.com')
        self.wait_for((By.XPATH, buissness_url_xpath)).send_keys('www.IQA.com')
        self.wait_for((By.XPATH, town_xpath)).send_keys('tel-aviv')
        self.wait_for((By.XPATH, street_xpath)).send_keys('rothschild')
        self.wait_for((By.XPATH, building_xpath)).send_keys('5')
        self.wait_for((By.XPATH, add_button)).click()

    def assert_upload_product(self):
        error_message_xpath = '/html/body/div/div/div[4]/div/div/div/div[2]/div[3]/form/div[3]'
        return self.wait_for((By.XPATH, error_message_xpath))

    def assert_product_title(self):
        title_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/h1'
        return self.wait_for((By.XPATH, title_xpath))

    def assert_product_carton(self):
        container_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/span'
        return self.wait_for((By.XPATH, container_xpath))

    def assert_cost_per_carton(self):
        container_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[3]/div/div[3]'
        return self.wait_for((By.XPATH, container_xpath))

    def assert_cartons_stock(self):
        container_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[3]/div/div[1]'
        return self.wait_for((By.XPATH, container_xpath))

    def add_product_to_cart_for_checkout(self):
        product_add_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div/div/span[1]/i'
        self.wait_for((By.XPATH, product_add_xpath)).click()

    def Empty_cart_button(self):
        empty_cart_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]'
        self.wait_for((By.XPATH, empty_cart_xpath)).click()

    def assert_empty_cart(self):
        price_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[3]/div/h6[4]/span[2]'
        return self.wait_for((By.XPATH, price_xpath)).text



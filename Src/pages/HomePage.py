from selenium.webdriver.common.by import By
from selenium import webdriver
from common import CommonOps


class HomePage(CommonOps):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_save_button(self):
        welcome_save_button_xpath = '//*[@id="root"]/div/div[4]/div/div/div/button'
        click_save_button = self.wait_for((By.XPATH, welcome_save_button_xpath)).click()

    # click the left arrow on the commercial container
    def click_left_arrow(self):
        left_arrow_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/button[1]'
        click_left_arrow = self.wait_for((By.XPATH, left_arrow_xpath)).click()

    # for the test assertion if the next image is shown (it starts from a specific commercial when refreshed)
    def assert_left_arrow(self):
        commerical_image_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[9]/a'
        return self.wait_for((By.XPATH, commerical_image_xpath))

    def click_right_arrow(self):
        right_arrow_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/button[2]'
        click_right_arrow = self.wait_for((By.XPATH, right_arrow_xpath)).click()

    def assert_right_arrow(self):
        commercial_image_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[3]/a'
        return self.wait_for((By.XPATH, commercial_image_xpath))

    def send_details_to_commercial_man_with_tablet(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/ul/li[2]/a'
        self.wait_for((By.XPATH, commercial_xpath)).click()
        # form
        name = self.wait_for((By.XPATH,
                              '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[1]/div[1]/div[1]/span/input')).send_keys(
            "ada")
        last_name = self.wait_for((By.XPATH,
                                   '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[1]/div[1]/div[2]/span/input')).send_keys(
            "goren")
        phone = self.wait_for((By.XPATH,
                               '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[1]/div[1]/div[3]/span/input')).send_keys(
            "0556134754")
        city = self.wait_for((By.XPATH,
                              '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[2]/div[1]/div[1]/input')).send_keys(
            "tel aviv")
        number = self.wait_for((By.XPATH,
                                '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[2]/div[1]/div[2]/span/input')).send_keys(
            "5")
        buissness_name = self.wait_for((By.XPATH,
                                        '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[3]/div[1]/div[1]/span/input')).send_keys(
            "poison")
        detection = self.wait_for((By.XPATH,
                                   '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[3]/div[1]/div[2]/span/input')).send_keys(
            "6")
        zip_code = self.wait_for((By.XPATH,
                                  '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/div[2]/div[3]/div[1]/div[3]/span/input')).send_keys(
            "55543")
        send_button = self.wait_for((By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[2]/form/input')).click()

    def assert_commercial_man_with_tablet(self):
        sent_element = "sent-pass"
        return self.wait_for((By.ID, sent_element))

    def commercial_man_with_phone(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/ul/li[3]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_commercial_man_with_phone(self):
        join_id = "join-the-brotherhood"
        return self.wait_for((By.ID, join_id))

    def commercial_man_thumbs_up(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/ul/li[4]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_comercial_man_thumbs_up(self):
        layout_id = 'join-us'
        return self.wait_for((By.ID, layout_id))

    def commercial_man_with_packages(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/ul/li[5]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_commercial_man_with_packages(self):
        menu_id = 'menu-id'
        return self.wait_for((By.ID, menu_id))

    def commercial_max_woman(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[6]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def commercial_girl_with_laptop(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[7]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def commercial_open_box(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[8]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_commercial_open_box(self):
        box_menu_id = 'box-menu'
        return self.wait_for((By.ID, box_menu_id))

    def commercial_woman_with_smoothie(self):
        commercial_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/ul/li[9]/a'
        element = self.driver.find_element(By.XPATH, commercial_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def navigate_to_all_questions_contact_us_more_details(self):
        all_questions_button = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a'
        return self.wait_for((By.XPATH, all_questions_button)).click()

    def get_list_elements(self):
        container_elements = self.driver.find_element(By.CSS_SELECTOR,
                                                      "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list")
        product_element = container_elements.find_elements(By.CSS_SELECTOR,
                                                           "#root > div > div.pages_pages > div.pages_children.false > div > div > div.store_productsList > div > div.productsList_productListWrapper > div.productsList_list > a:nth-child(1)")

        elem = []
        for prod in product_element:
            elem.append(prod)

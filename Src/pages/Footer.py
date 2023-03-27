from common import CommonOps
from selenium.webdriver.common.by import By



class Footer(CommonOps):

    def navigate_to_facebook(self):
        facebook_button_xpath = '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/a[1]'
        element = self.wait_for((By.XPATH, facebook_button_xpath))
        element.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
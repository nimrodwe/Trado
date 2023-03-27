from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonOps:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self.welcome_button = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')


    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def save_welcome_button(self):
        welcome_button = self._wait.until(EC.presence_of_element_located(self.welcome_button))
        welcome_button.click()



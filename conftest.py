import pytest
from selenium import webdriver
@pytest.fixture
def test_setup():
    driver = webdriver.Chrome()
    driver.get("https://qa.trado.co.il/")
    driver.maximize_window()

    yield driver
    driver.close()
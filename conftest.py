import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    #open chrome broswer
    driver = webdriver.Chrome()
    # maximize window
    driver.maximize_window()
    #give the browser driver to the test
    yield driver
    #close the driver after the test is completed
    driver.quit()

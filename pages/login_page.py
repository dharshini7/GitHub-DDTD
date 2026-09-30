

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # orange hrm login page
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    def __init__(self,driver):
        self.driver = driver
    # create an explicit wait of 10 seconds
        self.wait = WebDriverWait(driver,10)
    def enter_username(self,username):
    # wait untill userfield is visible and enter username
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        username_field.clear()
        username_field.send_keys(username)

    # wait until password field is visible and enter password
    def enter_password(self,password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        # wait until login button is clickable and click it

        login_button =  self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        login_button.click()
    def login(self,username,password):
        # perform complete login operation
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    def is_login_successful(self):
        # check whether the dashboard url is displayed after login
        # return "dashboard" in self.driver.current_url
        try:
            # wait untill the URL contains dashboard
            self.wait.until(EC.url_contains("/dashboard"))
            return True
        except:
            return False
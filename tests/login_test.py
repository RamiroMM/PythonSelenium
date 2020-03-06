from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import Properties as Prop


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(Prop.URL)

        login = LoginPage(driver)
        login.enter_username(Prop.USER)
        login.enter_password(Prop.PASSWORD)
        login.click_login_button()

    def test_logout(self):
        driver = self.driver
        time.sleep(2)
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

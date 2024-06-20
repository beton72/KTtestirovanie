
import pytest
import allure
from selenium import webdriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://dns-shop.ru/login")

    def set_username(self, username):
        self.driver.find_element_by_id("username").send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id("password").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id("login-btn").click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return "Welcome" in self.driver.title

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Login")
@pytest.mark.parametrize("username, password", [("user1", "password1"), ("user2", "password2")])
def test_login(browser, username, password):
    with allure.step("Open login page"):
        login_page = LoginPage(browser)
        login_page.open()

    with allure.step("Enter username and password"):
        login_page.set_username(username)
        login_page.set_password(password)

    with allure.step("Click login button"):
        login_page.click_login()

    with allure.step("Verify login successful"):
        home_page = HomePage(browser)
        assert home_page.is_loaded()

@allure.feature("Additional Functionality")
def test_additional_functionality_1(browser):
    with allure.step("Execute additional functionality test 1"):
        browser.get("http://dns-shop.ru/additional_functionality_1")
        assert browser.find_element_by_id("element_id_1").is_displayed()

@allure.feature("Additional Functionality")
def test_additional_functionality_2(browser):
    with allure.step("Execute additional functionality test 2"):
        browser.get("http://dns-shop.ru/additional_functionality_2")
        assert browser.find_element_by_class_name("element_class_2").is_displayed()

@allure.feature("Some Additional Feature")
def test_some_feature(browser):
    with allure.step("Execute some additional feature test"):
        browser.get("http://dns-shop.ru/some_additional_feature")
        assert "Some Additional Feature" in browser.page_source

if __name__ == "__main__":
    pytest.main(["-s", "-v", "--alluredir=allure-results"])

import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'US'
}

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def click_element(self, xpath):
        el = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        el.click()

    def delete_all(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="delete"]')
        el.click()

    def test_plus(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_7"]')
        self.click_element('//android.widget.Button[@content-desc="plus"]')
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_5"]')
        self.delete_all()

    def test_minus(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_9"]')
        self.click_element('//android.widget.Button[@content-desc="minus"]')
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_2"]')
        self.delete_all()

    def test_multiplication(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_4"]')
        self.click_element('//android.widget.Button[@content-desc="×"]')
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_8"]')
        self.delete_all()

    def test_divide(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_1"]')
        self.click_element('//android.widget.Button[@content-desc="divide"]')
        self.click_element('//android.widget.Button[@resource-id="com.android.calculator:id/digit_2"]')
        self.delete_all()

if __name__ == '__main__':
    unittest.main()
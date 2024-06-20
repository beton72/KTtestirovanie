from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://testingkt5max.com/opencart/admin/")
driver.find_element_by_id("input-username").send_keys("ваш_логин")
driver.find_element_by_id("input-password").send_keys("ваш_пароль")
driver.find_element_by_css_selector(".btn-primary").click()

driver.find_element_by_id("menu-catalog").click()
driver.find_element_by_xpath("//a[contains(text(),'Categories')]").click()
driver.find_element_by_css_selector(".fa-plus").click()
driver.find_element_by_id("input-name1").send_keys("Devices")
driver.find_element_by_css_selector(".btn-primary").click()


driver.find_element_by_id("menu-catalog").click()
driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
driver.find_element_by_css_selector(".fa-plus").click()

driver.find_element_by_id("input-name1").send_keys("Компьютерная мышь")
driver.find_element_by_css_selector("#language1 > .NoteRow > .note-editable").send_keys("Описание для мыши")
driver.find_element_by_css_selector(".fa-save").click()

driver.find_element_by_css_selector(".fa-plus").click()
driver.find_element_by_id("input-name1").send_keys("Клавиатура")
driver.find_element_by_css_selector("#language1 > .NoteRow > .note-editable").send_keys("Описание для клавиатуры")
driver.find_element_by_css_selector(".fa-save").click()

driver.get("http://testingkt5max.com/")
driver.find_element_by_name("search").send_keys("Компьютерная мышь" + Keys.RETURN)
time.sleep(2)
assert "Компьютерная мышь" in driver.page_source
driver.find_element_by_name("search").clear()
driver.find_element_by_name("search").send_keys("Клавиатура" + Keys.RETURN)
time.sleep(2)
assert "Клавиатура" in driver.page_source

driver.get("http://testingkt5max.com/opencart/admin/")
driver.find_element_by_id("menu-catalog").click()
driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()

driver.find_element_by_name("filter_name").send_keys("Компьютерная мышь" + Keys.RETURN)
time.sleep(2)
driver.find_element_by_css_selector(".fa-trash-o").click()
driver.switch_to.alert.accept()

driver.find_element_by_name("filter_name").clear()
driver.find_element_by_name("filter_name").send_keys("Клавиатура" + Keys.RETURN)
time.sleep(2)
driver.find_element_by_css_selector(".fa-trash-o").click()
driver.switch_to.alert.accept()

driver.get("http://testingkt5max.com/")
assert "Компьютерная мышь" not in driver.page_source
assert "Клавиатура" not in driver.page_source


driver.quit()
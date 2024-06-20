from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wdwait
from selenium.webdriver.support import expected_conditions as expcon


def main():
    driver = wd.Chrome()
    driver.get("http://localhost")
    wait = wdwait(driver, 100)
    wait.until(expcon.title_contains("Online Computer Store"))
    product_element = wait.until(expcon.presence_of_element_located((By.XPATH, "//div[@class='product']")))
    product_element.click()
    screenshot_element = wait.until(expcon.presence_of_element_located((By.XPATH, "//div[@class='screenshot']")))
    driver.save_screenshot("screenshot.png")
    screenshot_element.click()
    currency_select = Select(driver.find_element(By.ID, "currency-select"))
    currency_select.select_by_value("USD")
    pc_menu_item = wait.until(
        expcon.element_to_be_clickable((By.XPATH, "//li[@class='menu-item']/a[contains(text(), 'PC')]")))
    pc_menu_item.click()
    registration_link = wait.until(expcon.element_to_be_clickable((By.XPATH, "//a[@href='/registration']")))
    registration_link.click()

    search_keyword = "search_keyword"
    search_input = driver.find_element(By.ID, "search-input")
    search_input.send_keys(search_keyword)
    search_input.submit()
    search_button = driver.find_element(By.ID, "search-button")
    search_button.click()

    driver.quit()


if __name__ == "__main__":
    main()
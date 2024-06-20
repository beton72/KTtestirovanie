from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdwait
from selenium.webdriver.support import expected_conditions as expcon

driver = wd.Firefox()

driver.get("https://demo.opencart.com/")

try:
    product_link = driver.find_element_by_css_selector(".product-layout:first-child .product-thumb")
    product_link.click()

    screenshots = driver.find_elements_by_css_selector(".thumbnail")
    for screenshot in screenshots:
        screenshot.click()
        driver.save_screenshot("screenshot.png")
        driver.back()

    currency_dropdown = driver.find_element_by_css_selector("#form-currency")
    currency_dropdown.click()
    wdwait(driver, 10).until(expcon.element_to_be_clickable((By.NAME, 'EUR'))).click()
    wdwait(driver, 10).until(expcon.element_to_be_clickable((By.NAME, 'USD'))).click()

    pc_category_link = driver.find_element_by_css_selector("#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a")
    pc_category_link.click()

    empty_page_message = driver.find_element_by_css_selector(".alert.alert-info")
    if empty_page_message.is_displayed():
        print("страница 'PC' пустая")
    else:
        print("на странице 'PC' есть контент")

    registration_link = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?route=account/register']")
    registration_link.click()

    telephone_input = driver.find_element(By.ID, "input-telephone")
    telephone_input.send_keys("+77489012224")

    address_input = driver.find_element(By.ID, "input-address-1")
    address_input.send_keys("Derevnia Golyboe Tveretski proezd")

    city_input = driver.find_element(By.ID, "input-city")
    city_input.send_keys("Solnechogorsk")

    lastname_input = driver.find_element(By.ID, "input-lastname")
    lastname_input.send_keys("Kustov")

    region_input = driver.find_element(By.ID, "input-zone")
    region_input.send_keys("Moscow blast")

    password_input = driver.find_element(By.ID, "input-password")
    password_input.send_keys("password")

    confirm_password_input = driver.find_element(By.ID, "input-confirm")
    confirm_password_input.send_keys("password")

    email_input = driver.find_element(By.ID, "input-email")
    email_input.send_keys("kustovnm21@st.ithub.ru")

    country_input = driver.find_element(By.ID, "input-country")
    country_input.send_keys("Russian Federation")

    postcode_input = driver.find_element(By.ID, "input-postcode")
    postcode_input.send_keys("578201")

    firstname_input = driver.find_element(By.ID, "input-firstname")
    firstname_input.send_keys("Nikolay")

    register_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
    register_button.click()

except Exception as exp:
    print("Произошла ошибка:", exp)

finally:
    driver.quit()
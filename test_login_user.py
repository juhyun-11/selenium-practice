
from selenium.webdriver.common.by import By
from pages import wait_for

def test_login(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

    assert "Login to your account" in driver.page_source

    driver.find_element(By.NAME, "email").send_keys("test990$@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("asdf1234!")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']").click()

    logged_in = wait_for(driver, By.CSS_SELECTOR, "li a b")
    assert logged_in.text == "juhyuns"
    
    delete_btn=driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']")
    driver.execute_script("arguments[0].click();",delete_btn)

    deleted = wait_for(driver, By.CSS_SELECTOR, ".title.text-center")
    assert deleted.text == "ACCOUNT DELETED!"

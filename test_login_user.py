from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def test_login():
    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com")

    time.sleep(2)
    
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

    assert "Login to your account" in driver.page_source

    driver.find_element(By.NAME, "email").send_keys("test2211@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("asdf1234!")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']").click()
    
    assert "Logged in as" in driver.page_source
    
    delete_btn=driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']")
    driver.execute_script("arguments[0].click();",delete_btn)

    time.sleep(3)

    assert "Account Deleted" in driver.page_source
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")

    time.sleep(2)
    
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

    assert "Login to your account" in driver.page_source

    driver.find_element(By.CSS_SELECTOR, "[data-qa='login-email']").send_keys("test2223@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='login-password']").send_keys("asdf1234!")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']").click()
    
    assert "Logged in as" in driver.page_source
    
    logout_btn=driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
    driver.execute_script("arguments[0].click();",logout_btn)

    assert "login" in driver.current_url

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def test_cartpage():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")

    time.sleep(2)
    cart_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", cart_btn)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    assert "Subscription" in driver.page_source

    driver.find_element(By.ID, "susbscribe_email").send_keys("test2026@naver.com")
    subscribe_btn = driver.find_element(By.ID, "subscribe")
    driver.execute_script("arguments[0].click();", subscribe_btn)

    assert "You have been successfully subscribed!" in driver.page_source

    time.sleep(2)


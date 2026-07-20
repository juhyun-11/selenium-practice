from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import wait_for
import time

def test_add_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    pw = driver.find_element(By.ID, "password")
    pw.send_keys("secret_sauce")

    lg_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
    driver.execute_script("arguments[0].click();", lg_btn)

    title = wait_for(driver, By.CSS_SELECTOR, ".title")
    assert title.text == "Products" 

    product = driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    product.click()
    cart_btn = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_btn.click()


    title = wait_for(driver, By.CSS_SELECTOR, "#item_1_title_link")
    assert title.text == "Sauce Labs Bolt T-Shirt"








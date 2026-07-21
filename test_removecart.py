from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import wait_for, wait_invisible
import time

def test_remove_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    lg_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
    lg_btn.click()
    
    title = wait_for(driver, By.CSS_SELECTOR, ".title")
    assert title.text == "Products" 
    product = wait_for(driver, By.CSS_SELECTOR, 
                       "[data-test='add-to-cart-sauce-labs-bike-light']")
    product.click()
    cart_btn = wait_for(driver, By.CLASS_NAME, "shopping_cart_link")
    cart_btn.click()

    title = wait_for(driver, By.CSS_SELECTOR, "#item_0_title_link")
    assert title.text == "Sauce Labs Bike Light"


    remove = wait_for(driver, By.CSS_SELECTOR, 
                      ".btn.btn_secondary.btn_small.cart_button")
    remove.click()

    #remove 클릭 후 장바구니 배지 조회
    wait_invisible(driver, By.CLASS_NAME, "shopping_cart_badge")
    after_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(after_badge) == 0

    ctn_shopping = wait_for(driver, By.ID, 
                      "continue-shopping")
    ctn_shopping.click()


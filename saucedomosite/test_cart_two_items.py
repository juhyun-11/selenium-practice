from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import wait_for

def test_cart_two_items(driver):

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    
    lg_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
    lg_btn.click()

    add_cart = wait_for(driver, By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")
    add_cart.click()
    badge = wait_for(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    add_cart = wait_for(driver, By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    add_cart.click()
    badge = wait_for(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "2"

    cart = wait_for(driver, By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    cart.click()
    wait_for(driver, By.CSS_SELECTOR, "[data-test='checkout']")  # 장바구니 페이지에만 있는 버튼


    #여러 요소를 가져오는 find_elements를 활용해 상품 2개 확인
    item = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(item) == 2
    assert item[0].text == "Sauce Labs Bike Light"
    assert item[1].text == "Sauce Labs Bolt T-Shirt"

    remove_btn = wait_for(driver, By.CSS_SELECTOR, "[data-test='remove-sauce-labs-bike-light']" )
    remove_btn.click()
    badge = wait_for(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    remaining_item = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(remaining_item) == 1
    assert remaining_item[0].text == "Sauce Labs Bolt T-Shirt"

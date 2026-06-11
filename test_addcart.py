from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

def test_addcart(driver):
    prt_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", prt_btn)
    product = driver.find_element(By.CSS_SELECTOR, ".product-overlay")
    ActionChains(driver).move_to_element(product).perform()

    add_to_cart = driver.find_element(By.CSS_SELECTOR, "a[data-product-id='1']")
    driver.execute_script("arguments[0].click();", add_to_cart)

    time.sleep(2)

    assert "Added!" in driver.page_source

    ctn_btn = driver.find_element(By.CSS_SELECTOR, "[data-dismiss='modal']")
    driver.execute_script("arguments[0].click();", ctn_btn)
    product = driver.find_element(By.CSS_SELECTOR, ".product-overlay")
    ActionChains(driver).move_to_element(product).perform()

    add_to_cart = driver.find_element(By.CSS_SELECTOR, "a[data-product-id='2']")
    driver.execute_script("arguments[0].click();", add_to_cart)

    cart_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", cart_btn)

    assert "Blue Top" in driver.page_source
    assert "Rs. 500" in driver.page_source
    assert "Men Tshirt" in driver.page_source
    assert "Rs. 400" in driver.page_source
    quantity = driver.find_element(By.CSS_SELECTOR, ".cart_quantity button")
    assert  quantity.text == "1"


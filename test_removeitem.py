from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages import add_product_to_cart, wait_for

import time
def test_removeitem(driver):
    
    assert "Home" in driver.page_source
    add_product_to_cart(driver,8)

    ctn_btn = wait_for(driver, By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
    driver.execute_script("arguments[0].click();", ctn_btn)

    cart_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", cart_btn)

    assert "Fancy Green Top" in driver.page_source

    close_btn = wait_for(driver, By.CSS_SELECTOR, ".fa.fa-times")
    driver.execute_script("arguments[0].click();", close_btn)

    wait_for(driver, By.ID, "empty_cart")
    assert "Cart is empty!" in driver.page_source
    #id가 있으면 → By.ID ✅
    #name이 있으면 → By.NAME
    #id가 없으면 → CSS Selector
    #XPath는 정말 필요할 때만#






   


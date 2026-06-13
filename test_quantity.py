from selenium.webdriver.common.by import By
from pages import go_to_cart

import time

def test_quantity(driver):
    product_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/3']")
    driver.execute_script("arguments[0].click();", product_btn)

    assert 'Sleeveless Dress' in driver.page_source
    qty_input = driver.find_element(By.ID, "quantity")
    qty_input.clear()       # 먼저 "1" 지우기 → 빈칸
    qty_input.send_keys("4") 


    buttons = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-default.cart")
    
    addcart_btn = buttons[0]
    driver.execute_script("arguments[0].click();", addcart_btn)
    
    time.sleep(2)
    
    assert "Added!" in driver.page_source
    go_to_cart(driver)

    time.sleep(2)

    assert "Sleeveless Dress" in driver.page_source
    quantity = driver.find_element(By.CSS_SELECTOR, ".cart_quantity button")
    assert  quantity.text == "4"




from selenium.webdriver.common.by import By
from pages import go_to_cart, wait_for


def test_quantity(driver):
    product_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/3']")
    driver.execute_script("arguments[0].click();", product_btn)
    
   
    wait_for(driver, By.CSS_SELECTOR, ".product-information") #<div class="modal-header">여기서 class니까 .
    
    assert 'Sleeveless' in driver.page_source
    
    qty_input = driver.find_element(By.ID, "quantity")
    qty_input.clear()       # 먼저 "1" 지우기 → 빈칸
    qty_input.send_keys("4") 


    buttons = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-default.cart")
    
    addcart_btn = buttons[0]
    driver.execute_script("arguments[0].click();", addcart_btn)
    
    wait_for(driver, By.CSS_SELECTOR, ".modal-header") #<div class="modal-header">여기서 class니까 .
    assert "Added!" in driver.page_source
    
    go_to_cart(driver)
    product_name = wait_for(driver, By.CSS_SELECTOR, "a[href='/product_details/3")
    assert product_name.text == "Sleeveless Dress"

    quantity = wait_for(driver, By.CSS_SELECTOR, ".cart_quantity button")
    assert  quantity.text == "4"




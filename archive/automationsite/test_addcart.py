from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages import go_to_cart, add_product_to_cart, wait_for


def test_addcart(driver):
    prt_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", prt_btn)
    product = driver.find_element(By.CSS_SELECTOR, ".product-overlay")
    ActionChains(driver).move_to_element(product).perform()

    add_product_to_cart(driver,1)

    wait_for(driver, By.CSS_SELECTOR, "[data-dismiss='modal']")
    assert "Added!" in driver.page_source

    ctn_btn = driver.find_element(By.CSS_SELECTOR, "[data-dismiss='modal']")
    driver.execute_script("arguments[0].click();", ctn_btn)
    product = driver.find_element(By.CSS_SELECTOR, ".product-overlay")
    ActionChains(driver).move_to_element(product).perform()

    add_product_to_cart(driver, 2)

    go_to_cart(driver)

    assert "Blue Top" in driver.page_source
    assert "Rs. 500" in driver.page_source
    assert "Men Tshirt" in driver.page_source
    assert "Rs. 400" in driver.page_source
    quantity = driver.find_element(By.CSS_SELECTOR, ".cart_quantity button")
    assert  quantity.text == "1"


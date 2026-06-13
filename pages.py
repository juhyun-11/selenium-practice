#pages.py
from selenium.webdriver.common.by import By

def go_to_cart(driver):
    btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", btn)

def add_product_to_cart(driver, product_id):
    btn = driver.find_element(By.CSS_SELECTOR, f"a[data-product-id='{product_id}']")
    driver.execute_script("arguments[0].click();", btn)
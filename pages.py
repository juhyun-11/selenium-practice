#pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value)))

def go_to_cart(driver):
    btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", btn)

def add_product_to_cart(driver, product_id):
    btn = driver.find_element(By.CSS_SELECTOR, f"a[data-product-id='{product_id}']")
    driver.execute_script("arguments[0].click();", btn)


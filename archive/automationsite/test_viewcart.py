from selenium.webdriver.common.by import By
from pages import wait_for

def test_brand(driver):
    prd_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", prd_btn)

    title = wait_for(driver, By.CSS_SELECTOR, ".brands_products")
    # div 전체이기 때문에 브랜드다나와서 == 하면 실패. 
    assert "BRANDS" in title.text #부분 문자열만 확인
    
    brand_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/brand_products/Polo']")
    driver.execute_script("arguments[0].click();", brand_btn)

    title = wait_for(driver, By.CSS_SELECTOR, "h2.title.text-center")
    assert "BRAND - POLO PRODUCTS" in title.text

    brand2_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/brand_products/Biba']")
    driver.execute_script("arguments[0].click();", brand2_btn)

    title = wait_for(driver, By.CSS_SELECTOR, "h2.title.text-center")
    assert "BRAND - BIBA PRODUCTS" in title.text
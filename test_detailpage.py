from selenium.webdriver.common.by import By

import time

def test_detailpage(driver):

    pd_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", pd_btn)

    assert "All Products" in driver.page_source
    time.sleep(2)

    detail_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']")
    driver.execute_script("arguments[0].click();", detail_btn)

    time.sleep(4)

    pd_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", pd_btn)
    driver.find_element(By.ID, "search_product").send_keys("Dress")
    search_btn = driver.find_element(By.ID, "submit_search")
    driver.execute_script("arguments[0].click();", search_btn)
    assert "Searched Products" in driver.page_source

    time.sleep(3)

    home_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/']")
    driver.execute_script("arguments[0].click();", home_btn)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    assert "Subscription" in driver.page_source

    
    driver.find_element(By.ID, "susbscribe_email").send_keys("test2026@naver.com")
    subscribe_btn = driver.find_element(By.ID, "subscribe")
    driver.execute_script("arguments[0].click();", subscribe_btn)

    assert "You have been successfully subscribed!" in driver.page_source

    time.sleep(2)







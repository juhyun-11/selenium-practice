from selenium.webdriver.common.by import By
from pages import wait_for

def test_addreview(driver):
    prd_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/products']")
    driver.execute_script("arguments[0].click();", prd_btn)

    title = wait_for(driver, By.CSS_SELECTOR, ".title.text-center")
    assert "ALL PRODUCTS" in title.text

    view_btn = wait_for(driver, By.CSS_SELECTOR, "a[href='/product_details/1']")
    driver.execute_script("arguments[0].click();", view_btn)

    wait_for(driver, By.CSS_SELECTOR, ".nav.nav-tabs")
    assert "Write Your Review" in driver.page_source

    wait_for(driver, By.ID, "name").send_keys("joojoo")
    wait_for(driver, By.ID, "email").send_keys("test2002!@gmail.com")
    wait_for(driver, By.ID, "review").send_keys("오늘의 리뷰 작성 테스트입니다")
    submit_btn = wait_for(driver, By.ID, "button-review")
    driver.execute_script("arguments[0].click();", submit_btn)

    success = wait_for(driver, By.CSS_SELECTOR, ".alert-success.alert")
    assert "Thank you for your review." in success.text

    








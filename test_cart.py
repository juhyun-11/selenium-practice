from selenium.webdriver.common.by import By
from pages import wait_for

def test_cartpage(driver):
    cart_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", cart_btn)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    assert "Subscription" in driver.page_source

    driver.find_element(By.ID, "susbscribe_email").send_keys("test2026@naver.com")
    subscribe_btn = driver.find_element(By.ID, "subscribe")
    driver.execute_script("arguments[0].click();", subscribe_btn)

    wait_for(driver, By.CSS_SELECTOR, "#success-subscribe .alert-success")
    # #는 id가 "success-subscribe"인 element를 찾아라
    # id 앞엔 #, class 앞엔 . 이게 CSS 선택자 규칙, 띄어쓰기는 "안에 있는" 
    # id가 success-subscribe인 element 안에 있는 class가 alert-success인 element
    # <div id="success-subscribe">        ← #success-subscribe
    # <div class="alert-success">     ← .alert-success (안에 있는)

    assert "You have been successfully subscribed!" in driver.page_source



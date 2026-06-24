from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages import add_product_to_cart


import time


def test_order(driver):
    product = driver.find_element(By.CSS_SELECTOR, ".product-overlay")
    ActionChains(driver).move_to_element(product).perform()

    add_product_to_cart(driver,4)

    time.sleep(2)

    continue_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
    driver.execute_script("arguments[0].click();", continue_btn)

    time.sleep(2)

    cart_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
    driver.execute_script("arguments[0].click();", cart_btn)

    assert "Stylish Dress" in driver.page_source

    time.sleep(2)
    proceed_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out")
    driver.execute_script("arguments[0].click();", proceed_btn)

    time.sleep(2)

    lg_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
    driver.execute_script("arguments[0].click();", lg_btn)

    driver.find_element(By.NAME, "name").send_keys("juhyun")
    signup_email = f"test{int(time.time())}@gmail.com" 
    driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']").send_keys(signup_email)
    
    signup_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']")
    driver.execute_script("arguments[0].click();", signup_btn)
    

    radio = driver.find_element(By.ID, "id_gender2")
    driver.execute_script("arguments[0].click();", radio)
    driver.find_element(By.ID, "password").send_keys("asdf1234!")
    Select(driver.find_element(By.ID, "days")).select_by_value("22")
    Select(driver.find_element(By.ID, "months")).select_by_value("12")
    Select(driver.find_element(By.ID, "years")).select_by_value("1988")
    optin = driver.find_element(By.ID, "optin")
    driver.execute_script("arguments[0].click();", optin)

    time.sleep(2)

    driver.find_element(By.ID, "first_name").send_keys("juhyun")
    driver.find_element(By.ID, "last_name").send_keys("Jang")
    driver.find_element(By.ID, "company").send_keys("BCcard")
    driver.find_element(By.ID, "address1").send_keys("jakokro202")
    Select(driver.find_element(By.ID, "country")).select_by_value("United States")
    driver.find_element(By.ID, "state").send_keys("newyork")
    driver.find_element(By.ID, "city").send_keys("newyork")
    driver.find_element(By.ID, "zipcode").send_keys("10001")
    driver.find_element(By.ID, "mobile_number").send_keys("00000000001")
    create_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='create-account']")
    driver.execute_script("arguments[0].click();", create_btn)

    assert "Account Created!" in driver.page_source

    continue_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']")
    driver.execute_script("arguments[0].click();", continue_btn)

    assert "Logged in as" in driver.page_source
    assert "juhyun" in driver.page_source


    cart_btn = driver.find_element(By.LINK_TEXT, "Cart")
    cart_btn.click()
    
    proceed_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out")
    driver.execute_script("arguments[0].click();", proceed_btn)

    assert "Address Details" in driver.page_source
    assert "Review Your Order" in driver.page_source

    driver.find_element(By.NAME, "message").send_keys("오늘 테스트 중입니다")
    place_order = driver.find_element(By.CSS_SELECTOR, "a[href='/payment']")
    driver.execute_script("arguments[0].click();", place_order)

    pay_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='pay-button']")
    driver.execute_script("arguments[0].click();", pay_btn)
    driver.find_element(By.NAME, "name_on_card").send_keys("juhyun")
    pay_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='pay-button']")
    driver.execute_script("arguments[0].click();", pay_btn)
    driver.find_element(By.NAME, "card_number").send_keys("1234566788")
    pay_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='pay-button']")
    driver.execute_script("arguments[0].click();", pay_btn)
    driver.find_element(By.NAME, "cvc").send_keys("098765")
    pay_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='pay-button']")
    driver.execute_script("arguments[0].click();", pay_btn)
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    pay_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='pay-button']")
    driver.execute_script("arguments[0].click();", pay_btn)
    driver.find_element(By.NAME, "expiry_year").send_keys("2027")
    pay_btn = driver.find_element(By.CSS_SELECTOR, "[data-qa='pay-button']")
    driver.execute_script("arguments[0].click();", pay_btn)

    time.sleep(3)

    

    delete_account = driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']")
    driver.execute_script("arguments[0].click();", delete_account)

    assert "Account Deleted!" in driver.page_source

    












from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_contactusform(driver):
    driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']").click()

    assert "Get In Touch" in driver.page_source

    driver.find_element(By.NAME,"name").send_keys("juhyun")
    driver.find_element(By.NAME, "email").send_keys("test8888@gmail.com")
    driver.find_element(By.NAME, "subject").send_keys("question")
    driver.find_element(By.ID, "message").send_keys("I have a question about automation")
    driver.find_element(By.NAME, "upload_file").send_keys("/Users/jangjuhyeon/Desktop/IMG_0016.PNG")
    
    submit_btn = driver.find_element(By.NAME, "submit")
    driver.execute_script("arguments[0].click();",submit_btn)
    alert =driver.switch_to.alert
    alert.accept()
    

    assert "Success! Your details have been submitted successfully." in driver.page_source

    home_btn = driver.find_element(By.CSS_SELECTOR, "[href='/']")
    driver.execute_script("arguments[0].click();",home_btn)

    tc_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
    driver.execute_script("arguments[0].click();", tc_btn)

    assert "Test Cases" in driver.page_source

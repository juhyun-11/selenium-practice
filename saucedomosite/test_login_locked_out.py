from selenium.webdriver.common.by import By
from pages import wait_for

def test_login_locked_out_user(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    lg_button = wait_for(driver, By.CSS_SELECTOR, "[data-test='login-button']")
    lg_button.click()

    alert = wait_for(driver, By.CSS_SELECTOR, "[data-test='error']")
    assert "locked out" in alert.text
    assert driver.current_url == "https://www.saucedemo.com/"

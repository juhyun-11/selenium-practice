
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages import wait_for

def test_register(driver):
  
    assert "Automation Exercise" in driver.title

    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

    assert "New User Signup!" in driver.page_source

    wait_for(driver, By.NAME, "name").send_keys("juhyuns")
    wait_for(driver, By.CSS_SELECTOR, "[data-qa='signup-email']").send_keys("test990$@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']").click()
   
    assert "Enter Account Information" in driver.page_source


    radio = wait_for(driver, By.ID, "id_gender2")
    driver.execute_script("arguments[0].click();", radio)
    driver.find_element(By.ID, "password").send_keys("asdf1234!")
    Select(driver.find_element(By.ID, "days")).select_by_value("22")
    Select(driver.find_element(By.ID, "months")).select_by_value("10")
    Select(driver.find_element(By.ID, "years")).select_by_value("1990")
    newsletter = driver.find_element(By.ID, "newsletter")
    driver.execute_script("arguments[0].click();", newsletter)

    driver.find_element(By.ID, "first_name").send_keys("juhyun")
    driver.find_element(By.ID, "last_name").send_keys("juhyun")
    driver.find_element(By.ID, "company").send_keys("photoism")
    driver.find_element(By.ID, "address1").send_keys("jakokro202")
    Select(driver.find_element(By.ID, "country")).select_by_value("United States")
    driver.find_element(By.ID, "state").send_keys("newyork")
    driver.find_element(By.ID, "city").send_keys("newyork")
    driver.find_element(By.ID, "zipcode").send_keys("10001")
    driver.find_element(By.ID, "mobile_number").send_keys("00000000000")
    create_btn = wait_for(driver, By.CSS_SELECTOR, "[data-qa='create-account']")
    driver.execute_script("arguments[0].click();", create_btn)

    assert "Account Created!" in driver.page_source
    
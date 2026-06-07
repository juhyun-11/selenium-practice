from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    time.sleep(4)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(4)

    assert "logged-in-successfully" in driver.current_url

    driver.quit()

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    time.sleep(4)

    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("assword123")
    driver.find_element(By.ID,"submit").click()

    time.sleep(4)

    assert "logged-in-successfully" in driver.current_url
    driver.quit()

def test_multiple_users():
    users =[ 
        {"id": "student","pw":"Password123"},
        {"id": "student","pw":"wrongpassword"},
    ]
    for user in users:
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        time.sleep(5)

        driver.find_element(By.ID,"username").send_keys(user["id"])
        driver.find_element(By.ID,"password").send_keys(user["pw"])
        driver.find_element(By.ID,"submit").click()

        time.sleep(5)

        driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def loginpage():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(ID, "user-name").send_keys("stanrd_user")
    driver.find_element(ID, "password").send_keys("secret_sauce")
    login_btn = driver.find_element(ID, "login_button")
    driver.execute_script("arguments[0].click();", login_btn)



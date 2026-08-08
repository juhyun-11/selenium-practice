import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    
    print(username.get_attribute("value"))
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    login_btn = driver.find_element(By.ID, "login-button")
    driver.execute_script("arguments[0].click();", login_btn)


    assert "inventory.html" in driver.current_ur
    


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import wait_for

def test_login(driver):

    driver.find_element(By,ID, "user-name").send_keys("standard_user")
    driver.find_element(By,ID, "password").send_keys("secret_sauce")
    login_btn = driver.find_element(By,ID, "login-button")
    driver.execute_script("arguments[0].click();", login_btn)

    wait_for(driver, By.CLASS_NAME, "inventory_list")
    assert "Products" in driver.page_source



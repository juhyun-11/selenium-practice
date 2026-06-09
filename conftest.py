#conftest.py
import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    time.sleep(2)
    yield driver
    driver.quit()
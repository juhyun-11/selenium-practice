#conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com")
    WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.TAG_NAME, "body")))
    yield driver
    driver.quit()